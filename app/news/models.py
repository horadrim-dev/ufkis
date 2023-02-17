from email.policy import default
from django.db import models
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from django.urls import reverse
from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PlaceholderField
import uuid
import datetime
from core.utils import slugify_rus
import locale

class ContentManager(models.Manager):

    def published(self):
        return self.filter(published=True, published_at__lte=datetime.date.today())

class Post(models.Model):
    title = models.CharField(
        default="", max_length=1000, verbose_name="Заголовок")
    alias = models.SlugField(default="", blank=True, unique=True,
                             max_length=1000, help_text="Краткое название транслитом через тире (пример: 'kratkoe-nazvanie-translitom'). Чем короче тем лучше. Для автоматического заполнения - оставьте пустым.")
    published = models.BooleanField(default=True, verbose_name='Опубликовано')
    published_at = models.DateField(default=datetime.date.today, 
                                    verbose_name="Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее изменение")

    text = HTMLField("Содержимое", default="", blank=True, null=True)

    image = FilerImageField(verbose_name="Изображение", on_delete=models.CASCADE)

    IMAGE_POSITION_CHOICES = [
        ('left', 'Слева'),
        ('stretch', 'Растянуть'),
        ('right', 'Справа'),
        ('hide', 'Скрыть'),
    ]
    image_position = models.CharField(max_length=64, choices=IMAGE_POSITION_CHOICES, default=IMAGE_POSITION_CHOICES[0][0],
        verbose_name="Расположение изображения")

    placeholder_top = PlaceholderField('top', related_name="post_top")
    placeholder_bottom = PlaceholderField('bottom', related_name="post_bottom")

    objects = ContentManager()

    @property
    def gen_id(self):
        return str(uuid.uuid4().fields[-1])[:7]

    def get_absolute_url(self):
        return reverse("news:detail", kwargs={"slug": self.alias})

    def __str__(self):
        return self.title

    def save(self, lock_recursion=False, *args, **kwargs):
        # только при создании объекта, id еще не существует
        if not self.id or not self.alias:
            # заполняем алиас
            self.alias = slugify_rus(self.title)

        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-published_at']


class NewsPlugin(CMSPlugin):

    num_objects = models.PositiveIntegerField("Количество новостей", default=3)

    def get_objects(self, limit):
        return Post.objects.published()[:limit]

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]