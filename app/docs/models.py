from django.db import models
from filer.fields.file import FilerFileField, File
from django.urls import reverse
from core.models import OrderedModel
import datetime
import uuid
from django.dispatch import receiver
import os

class ContentManager(models.Manager):

    def published(self):
        return self.filter(published=True, published_at__lte=datetime.date.today())
    

class Category(OrderedModel):

    name = models.CharField("Название категории", max_length=64)

    def save(self, lock_recursion=False, *args, **kwargs):

        super().save(*args, **kwargs)

        # save method для OrderedModel
        if not lock_recursion:
            self.update_order(
                list_of_objects = list(
                    Category.objects.all().exclude(id=self.id)
                    # Category.objects.filter(parent=self.parent).exclude(id=self.id)
                    )
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class DocumentType(OrderedModel):

    name = models.CharField("Название типа документа", max_length=64,
                            help_text="Распоряжение, постановление, приказ и т.д.")

    # todo: ПОЛЯ ТИПА ДОКУМЕНТА или не надо?
    # простой документ (без нихуя, только название)

    def save(self, lock_recursion=False, *args, **kwargs):

        super().save(*args, **kwargs)

        # save method для OrderedModel
        if not lock_recursion:
            self.update_order(
                list_of_objects = list(
                    DocumentType.objects.all().exclude(id=self.id)
                    # Category.objects.filter(parent=self.parent).exclude(id=self.id)
                    )
            )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "тип документа"
        verbose_name_plural = "типы документов"


class Document(models.Model):
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name="Категория")
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE,
                                 verbose_name="Тип документа")

    date = models.DateField("Дата", blank=True, null=True)
    number = models.CharField("Номер", max_length=32,
                              blank=True, null=True)
    name = models.CharField("Название", max_length=512,
                            blank=True, null=True)
    document_file = FilerFileField(verbose_name="Файл документа", on_delete=models.CASCADE,
                               blank=True, null=True)
    extension = models.CharField(default="", max_length=16, blank=True, null=True,
                                verbose_name="Расширение файла")
    document_url = models.URLField("Ссылка на документ", 
                                    blank=True, null=True)

    published_at = models.DateField(default=datetime.date.today, 
                                    verbose_name="Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее изменение")
    hits = models.PositiveIntegerField(default=0, verbose_name="Кол-во загрузок")

    objects = ContentManager()

    def save(self,  *args, **kwargs):
        # считываем расширение файла
        if self.document_file:
            self.extension = self.document_file.path.split('.')[-1].lower()

        super().save(*args, **kwargs)

    def url(self):
        '''Формирует url для скачивания'''
        # return reverse('document_download', kwargs={'uuid': self.uuid})
        if self.document_url:
            return self.document_url
        
        return reverse('docs:document_download', kwargs={'id': self.id})

    @property
    def full_name(self):
        return " ".join([
            str(self.document_type) if self.document_type else "",
            "№" + str(self.number) if self.number else "",
            "от " + str(self.date) if self.date else "",
            str(self.name) if self.name else ""
        ])

    @property
    def filename(self):
        return "{}.{}".format(self.full_name, self.extension)

    # @property
    # def extension(self):
    #     return self.document_file.path.split('.')[-1].lower() if self.document_file else ""

    def fa_icon(self):
        """Возвращает название иконки (font awesome 4.7) для файла документа """

        ARCHIVE = { "ext" : ("rar", "zip", "7z"),  "icon": "fa-file-archive-o"}
        WORD = {"ext": ("doc", "docx"), "icon": "fa-file-word-o"}
        EXCEL = {"ext": ("xls", "xlsx"), "icon": "fa-file-excel-o"}
        VIDEO = {"ext": ("mp4", "avi", "mkv"), "icon": "fa-file-video-o"}
        PDF = {"ext" : ("pdf", ), "icon": "fa-file-pdf-o"}

        file_types = [ARCHIVE, WORD, EXCEL, VIDEO, PDF]
        for file_type in file_types:
            if self.extension in file_type["ext"]:
                return file_type["icon"]

        return "fa-file-o"


    class Meta:
        verbose_name = "документ"
        verbose_name_plural = "документы"
        ordering = ["-published_at"]



@receiver(models.signals.post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Удаляет файл при удалении объекта
    """
    if instance.document_file:
        if os.path.isfile(instance.document_file.path):
            # delete file from file system
            os.remove(instance.document_file.path)
            # delete Filer File object
            File.objects.filter(id=instance.document_file_id).delete()