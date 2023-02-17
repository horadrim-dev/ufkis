from tabnanny import verbose
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from colorfield.fields import ColorField
import uuid


class ColorBlocksModel(CMSPlugin):


    def get_colorblocks(self):
        return self.colorblock_set.all()

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]

    def copy_relations(self, oldinstance):
        # Before copying related objects from the old instance, the ones
        # on the current one need to be deleted. Otherwise, duplicates may
        # appear on the public version of the page
        self.colorblock_set.all().delete()

        for slide in oldinstance.colorblock_set.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            slide.pk = None
            slide.plugin = self
            slide.save()

class ColorBlock(models.Model):
    plugin = models.ForeignKey(
            ColorBlocksModel,
            on_delete=models.CASCADE,
        )
    title = models.CharField("Заголовок", max_length=255, default="")
    text = models.CharField("Текст", max_length=1000, default="", blank=True, null=True)
    icon = models.CharField("Иконка", max_length=32, default="", blank=True, null=True, help_text="Названия иконок брать <a href=\"https://icons.getbootstrap.com/\" target=\_blank\">отсюда</a>")
    color = ColorField(default='#00BB00')
    order = models.PositiveIntegerField('Порядок', default=0)

    def __str__(self):
        return self.title if self.title else ""

    class Meta:
        verbose_name = "цветной блок"
        verbose_name_plural = "цветные блоки"
        ordering = ('order', )