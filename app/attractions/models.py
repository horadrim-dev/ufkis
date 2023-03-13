from email.policy import default
from tabnanny import verbose
from django.db import models
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from django.urls import reverse
from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PlaceholderField

from core.models import OrderedModel
import uuid

SEASON_CHOICES = (
    ('summer', 'Лето'),
    ('winter', 'Зима'),
)

class Category(models.Model):
    title = models.CharField("Название", max_length=256)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

class Attraction(OrderedModel):
    title = models.CharField("Название", max_length=255, default="")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.PositiveIntegerField('Цена, руб/билет (взрослый)', default=0)
    price_kid = models.PositiveIntegerField('Цена, руб/билет (дети)', default=0)
    rental_time = models.FloatField('Время проката, в минутах', default=0, help_text="(0 = без ограничений)")
    restrictions = models.CharField("Ограничения", max_length=1024, default="", blank=True, null=True)
    season = models.CharField('Сезон', max_length=16, choices=SEASON_CHOICES, default=SEASON_CHOICES[0][0])
    description = HTMLField("Описание", default="", blank=True, null=True)

    placeholder_top = PlaceholderField('top')
    placeholder_bottom = PlaceholderField('bottom', related_name="placeholder_bottom")

    main_photo = FilerImageField(
        verbose_name='Главное фото',
        on_delete=models.CASCADE, 
        blank=True, null=True
    )


    def get_photos(self):
        return self.photo_set.all()

    @property
    def gen_id(self):
        return str(uuid.uuid4().fields[-1])[:7]

    def get_absolute_url(self):
        return reverse("attractions:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    def save(self, lock_recursion=False, *args, **kwargs):

        super().save(*args, **kwargs)

        if not lock_recursion:
            self.update_order(
                list_of_objects = list(
                    Attraction.objects.filter(category=self.category, season=self.season).exclude(id=self.id)
                    )
            )

    class Meta:
        verbose_name = 'аттракцион'
        verbose_name_plural = 'аттракционы'
        ordering = ['order']

class Photo(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    image = FilerImageField(
        verbose_name='Фото',
        on_delete=models.CASCADE, 
    )

class AttractionsPlugin(CMSPlugin):

    num_objects = models.PositiveIntegerField("Количество аттракционов", default=4)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    # category = models.('Категория', max_length=16, choices=SEASON_CHOICES, default=SEASON_CHOICES[0][0])
    season = models.CharField('Сезон', max_length=16, choices=SEASON_CHOICES, default=SEASON_CHOICES[0][0], blank=True, null=True)

    def get_attractions(self, limit, category=None, season=None):
        qs = Attraction.objects.all()
        if category:
            qs = qs.filter(category=category)
        if season:
            qs = qs.filter(season=season)

        return qs[:limit]

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]