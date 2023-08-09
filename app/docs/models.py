from django.db import models
from filer.fields.file import FilerFileField
from django.urls import reverse
from core.models import OrderedModel
import datetime


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
    document_url = models.URLField("Ссылка на документ", 
                                    blank=True, null=True)

    published_at = models.DateField(default=datetime.date.today, 
                                    verbose_name="Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее изменение")

    objects = ContentManager()

    class Meta:
        verbose_name = "документ"
        verbose_name_plural = "документы"
        ordering = ["-published_at"]