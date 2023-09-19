from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
import datetime
from filer.fields.image import FilerImageField
from easy_thumbnails.files import get_thumbnailer
from django.urls import reverse, NoReverseMatch
from cms.models.pluginmodel import CMSPlugin
import uuid


class EventContentManager(models.Manager):

    def upcoming(self):
        return self.filter(start_at__gte=datetime.datetime.now())

    # def finished(self):
    #     return self.filter(published=True, start_at__lte=datetime.datetime.now())


class Event(models.Model):
    '''Модель мероприятия'''
    name = models.CharField("Название мероприятия", max_length=512)
    place = models.CharField("Место проведения", max_length=256, blank=True, null=True)
    start_at = models.DateTimeField(default=datetime.datetime.now, 
                                    verbose_name="Время начала мероприятия")
    # finish_at = models.DateTimeField(default=datetime.datetime.now, 
    #                                 verbose_name="Время окончания мероприятия")
    poster = FilerImageField(
        verbose_name="Обложка",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    description = HTMLField(verbose_name="Описание", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее изменение")

    objects = EventContentManager()

    class Meta:
        verbose_name = "мероприятие"
        verbose_name_plural = "мероприятия"
        ordering = ['start_at']


    def __str__(self):
        return self.name
    
    def poster_thumb_src(self):
        image = self.poster
        if not image:
            return None

        thumbnail_options = {
            'size': (360, 240),
            'crop': True,
            'upscale': True,
            'subject_location': image.subject_location,
        }
        thumbnailer = get_thumbnailer(image)
        return thumbnailer.get_thumbnail(thumbnail_options).url
    
    def get_absolute_url(self):
        try:
            return "{}?lightbox=event-{}".format(reverse("events:index"), self.id)
        except NoReverseMatch:
            return "#"
    

class UpcomingEventsPlugin(CMSPlugin):

    num_objects = models.PositiveIntegerField("Количество мероприятий", default=3)

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]