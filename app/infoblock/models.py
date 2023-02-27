from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from filer.models.imagemodels import Image
import uuid
from djangocms_text_ckeditor.fields import HTMLField
from colorfield.fields import ColorField

class Infoblock(CMSPlugin):


    def get_slides(self):
        return self.slide_set.all()

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]

    def copy_relations(self, oldinstance):
        # Before copying related objects from the old instance, the ones
        # on the current one need to be deleted. Otherwise, duplicates may
        # appear on the public version of the page
        self.slide_set.all().delete()

        for slide in oldinstance.slide_set.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            slide.pk = None
            slide.plugin = self
            slide.save()

class Slide(models.Model):
    plugin = models.ForeignKey(
            Infoblock,
            on_delete=models.CASCADE,
        )
    title = models.CharField("Заголовок", max_length=1024, default="", blank=True, null=True)
    description = HTMLField("Описание", default="", blank=True, null=True)
    background_color = ColorField(default='#FFFFFF', verbose_name="Цвет фона",
        blank=True, null=True
    )
    image = FilerImageField(
        verbose_name=_('Изображение'),
        on_delete=models.CASCADE,
    )
    # def __str__(self):
    #     return self.title if self.title else super(self)

    class Meta:
        verbose_name = "слайд"
        verbose_name_plural = "слайды"
