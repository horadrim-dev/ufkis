from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from colorfield.fields import ColorField
from djangocms_text_ckeditor.fields import HTMLField
import uuid

OVERLAY_OPACITY_CHOICES = [
    ('0', '0'),
    ('.1', '10%'),
    ('.25', '25%'),
    ('.5', '50%'),
    ('.75', '75%'),
    ('1', '100%'),
]

class BackgroundSection(CMSPlugin):

    title = models.CharField("Заголовок", max_length=255, default="", blank=True, null=True, help_text="Не обязательно")
    text = HTMLField("Текст", default="", blank=True, null=True, help_text="Не обязательно")
    text_bottom = HTMLField("Текст снизу секции", default="", blank=True, null=True, help_text="Не обязательно")

    background_image = FilerImageField(
        verbose_name=_('Фоновое изображение'),
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    thumb_width = models.PositiveSmallIntegerField("Ширина", default=0)
    thumb_height = models.PositiveSmallIntegerField("Высота", default=0)
    background_color = ColorField(default='#FFFFFF', verbose_name="Фоновый цвет", help_text="Опция будет проигнорирована, если задано фоновое изображение",
        blank=True, null=True
    )
    css_classes = models.CharField("CSS классы", max_length=256, help_text="указать классы через пробел", default="", blank=True, null=True)
    use_parallax = models.BooleanField(default=False, verbose_name="Использовать эффект параллакса")
    use_overlay = models.BooleanField(default=False, verbose_name="Использовать оверлей")
    overlay_color = ColorField(default='#FFFFFF', verbose_name="Цвет оверлея", help_text="Этот цвет будет накладываться на изображение",
        blank=True, null=True
    )
    overlay_opacity = models.CharField(
        max_length=8,
        verbose_name="Прозрачность оверлея",
        choices=OVERLAY_OPACITY_CHOICES,
        default='.5',
    )

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]

    def get_width_height_thumb(self):
        return "{}x{}".format(self.thumb_width, self.thumb_height)

    def __str__(self):
        return self.title if self.title else ''