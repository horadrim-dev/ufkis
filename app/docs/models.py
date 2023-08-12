from django.db import models
from filer.fields.file import FilerFileField, File
from django.urls import reverse
from core.models import OrderedModel
import datetime
import uuid
from django.dispatch import receiver
import os
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase, TagBase, GenericTaggedItemBase
from cms.models.pluginmodel import CMSPlugin

class ContentManager(models.Manager):

    def published(self):
        return self.filter(published=True, published_at__lte=datetime.date.today())
    

class Category(OrderedModel):

    name = models.CharField("Название категории", max_length=256)

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
    
    def get_absolute_url(self):
        return "{}?category={}".format(reverse("docs:index"), self.id)
    

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["order"]


# class DocumentType(OrderedModel):

#     name = models.CharField("Название типа документа", max_length=64,
#                             help_text="Распоряжение, постановление, приказ и т.д.")
#     show_document_type = models.BooleanField("Отображать тип документа, номер и дату (если они заданы) в названии",
#                                              default=True)
#     # todo: ПОЛЯ ТИПА ДОКУМЕНТА или не надо?
#     # простой документ (без нихуя, только название)

#     def save(self, lock_recursion=False, *args, **kwargs):

#         super().save(*args, **kwargs)

#         # save method для OrderedModel
#         if not lock_recursion:
#             self.update_order(
#                 list_of_objects = list(
#                     DocumentType.objects.all().exclude(id=self.id)
#                     # Category.objects.filter(parent=self.parent).exclude(id=self.id)
#                     )
#             )

#     def __str__(self):
#         return self.name
    
    class Meta:
        verbose_name = "тип документа"
        verbose_name_plural = "типы документов"


class Document(models.Model):
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name="Категория")
    # document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE,
    #                              verbose_name="Тип документа")

    name = models.CharField("Название документа", max_length=512, default="Документ",
                            help_text="Примеры: \"Приказ Минспорта РФ\" , \"Уставной документ\", и т.д.   Номер и дату в этом поле не указывайте")
    number = models.CharField("Номер", max_length=32,
                              blank=True, null=True,
                              help_text="Укажите номер документа (если он есть)")
    date = models.DateField("Дата", blank=True, null=True,
                            help_text="Укажите дату документа (если она есть)")
    subname = models.CharField("Описание документа", max_length=512,
                            blank=True, null=True,
                            help_text="Без внешних кавычек. Пример: Об утверждении правил перевозки детей. ")
    document_file = FilerFileField(verbose_name="Файл документа", on_delete=models.CASCADE,
                               blank=True, null=True)
    extension = models.CharField(default="", max_length=16, blank=True, null=True,
                                verbose_name="Расширение файла")
    document_url = models.URLField("Ссылка на документ", 
                                    blank=True, null=True)

    published_at = models.DateTimeField(default=datetime.datetime.now, 
                                    verbose_name="Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее изменение")
    hits = models.PositiveIntegerField(default=0, verbose_name="Кол-во загрузок")

    tags = TaggableManager()

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
        # if not self.document_type.show_document_type:
        #     return self.name

        return " ".join([
            str(self.name),
            "№" + str(self.number) if self.number else "",
            "от " + str(self.date) if self.date else "",
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


# LAYOUT_CHOICES = [("small", 'Маленький'), ("medium", "Средний"), ("large", "Большой")]
class DocumentsPlugin(CMSPlugin):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                 verbose_name="Категория")
    show_description = models.BooleanField("Отображать описание документов", default=False)
    show_icon = models.BooleanField("Отображать иконку документов", default=True)
    # show_link = models.BooleanField("Отображать кнопку ссылки на документ", default=True)
    show_file_attrs = models.BooleanField("Отображать атрибуты файла", default=True)
    show_tags = models.BooleanField("Отображать теги документа", default=False)
    # layout = models.CharField("Размер элементов", choices=LAYOUT_CHOICES, default=LAYOUT_CHOICES[-1][0])
    # num_objects_in_row = models.PositiveIntegerField("Количество объектов в строке", default=3)

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]
    
    def related_documents(self):
        return self.category.document_set.all()