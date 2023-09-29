from django.db import models
from cms.models.pluginmodel import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField

POPUP_POSITION_CHOICES = [
    ('bottom-right', 'Справа внизу'),
    ('top-left', 'Слева вверху'),
    ('top-right', 'Справа вверху'),
    ('bottom-left', 'Слева внизу'),
    ('bottom', 'Внизу во всю ширину'),
    ('top', 'Вверху во всю ширину'),
]
class Popup(CMSPlugin):
    layout = models.CharField("Расположение", choices=POPUP_POSITION_CHOICES,
                                default=POPUP_POSITION_CHOICES[0][0])
    title = models.CharField(max_length=256, blank=True, null=True)
    content = HTMLField("Содержимое")