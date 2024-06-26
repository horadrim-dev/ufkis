# Generated by Django 4.1.7 on 2023-06-02 03:14

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('news', '0011_alter_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='cover_image',
            field=filer.fields.image.FilerImageField(blank=True, help_text='Если не задано - будет использовано первое изображение из содержимого поста', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL, verbose_name='Обложка поста'),
        ),
    ]
