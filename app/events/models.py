from collections.abc import Iterable
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
import datetime
from filer.fields.image import FilerImageField
from easy_thumbnails.files import get_thumbnailer
from django.urls import reverse, NoReverseMatch
from cms.models.pluginmodel import CMSPlugin
import uuid
from django.utils import timezone


class CategoryEvent(models.Model):
    name = models.CharField("Название категории", max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория мероприятий"
        verbose_name_plural = "категории мероприятий"

class Event(models.Model):
    '''Модель мероприятия'''
    category = models.ForeignKey(CategoryEvent, verbose_name="Категория", 
                                 on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField("Название мероприятия", max_length=512)
    # place = models.CharField("Место проведения", max_length=256, blank=True, null=True)
    # start_at = models.DateTimeField(default=datetime.datetime.now, 
    #                                 verbose_name="Время начала мероприятия")
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

    # objects = EventContentManager()

    class Meta:
        verbose_name = "мероприятие"
        verbose_name_plural = "мероприятия"
        # ordering = ['start_at']

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     try:
    #         return "{}?lightbox=event-{}".format(reverse("events:index"), self.id)
    #     except NoReverseMatch:
    #         return "#"
    

class DayEventContentManager(models.Manager):

    def upcoming(self):
        return self.filter(start_at__gte=timezone.now())

    def upcoming_by_date(self, date):
        return self.upcoming().filter(start_at__date=date)
    # def finished(self):
    #     return self.filter(published=True, start_at__lte=datetime.datetime.now())

class DayEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start_at = models.DateTimeField(default=timezone.now, 
                                    verbose_name="Время начала мероприятия")
    place = models.CharField("Место проведения", max_length=256, blank=True, null=True)
    postfix_name = models.CharField("Постфикс названия мероприятия", blank=True, null=True,
                                    help_text="Пример: День 1, Второй этап и т.д. \
                                               Будет отображено в квадратных скобках в \
                                               конце названия мероприятия.")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее изменение")

    objects = DayEventContentManager()

    class Meta:
        verbose_name = "день"
        verbose_name_plural = "дни мероприятия"
        ordering = ['start_at']

    def __str__(self):
        return self.name

    @property
    def category(self):
        return self.event.category

    @property
    def poster(self):
        return self.event.poster

    @property
    def description(self):
        return self.event.description

    @property
    def name(self):
        if self.postfix_name:
            return "{} [{}]".format(self.event.name, self.postfix_name)
        else:
            return self.event.name

    def get_absolute_url(self):
        try:
            return "{}?lightbox=event-{}".format(reverse("events:index"), self.id)
        except NoReverseMatch:
            return "#"

    def poster_thumb_src(self):
        image = self.poster
        if not image:
            return None

        thumbnail_options = {
            'size': (360, 240),
            'crop': False,
            'upscale': True,
            'subject_location': image.subject_location,
        }
        thumbnailer = get_thumbnailer(image)
        return thumbnailer.get_thumbnail(thumbnail_options).url


class UpcomingEventsPlugin(CMSPlugin):

    num_objects = models.PositiveIntegerField("Количество мероприятий", default=3)
    category = models.ForeignKey(CategoryEvent, verbose_name="Категория", 
                                 on_delete=models.SET_NULL, blank=True, null=True)

    def get_objects(self):
        qs = DayEvent.objects.upcoming()
        if self.category:
            qs = qs.filter(event__category=self.category)
        if self.num_objects:
            qs = qs[:self.num_objects]
        return qs

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]


class CalendarEventsPlugin(CMSPlugin):

    # num_objects = models.PositiveIntegerField("Количество мероприятий", default=3)
    category = models.ForeignKey(CategoryEvent, verbose_name="Категория мероприятий", 
                        on_delete=models.SET_NULL, blank=True, null=True,
                        help_text="Оставьте пустым для использования всех категорий")

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]
    