from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from colorfield.fields import ColorField
from djangocms_text_ckeditor.fields import HTMLField
import uuid


class Breadcrumbs(CMSPlugin):

    _title = models.CharField("Заголовок", max_length=255, default="", 
                             blank=True, null=True, 
                             help_text="Не обязательно. Если не заполнено - будет использован заголовок страницы.")

    image = FilerImageField(
        verbose_name=_('Изображение'),
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    height = models.PositiveSmallIntegerField("Высота", default=300)

    @property
    def title(self):
        return self._title if self._title.strip() else None

    def get_width_height_thumb(self):
        # return "{}x{}".format(self.thumb_width, self.thumb_height)
        return "{}x{}".format(1200, self.height)

    def __str__(self):
        return self.__class__.__name__