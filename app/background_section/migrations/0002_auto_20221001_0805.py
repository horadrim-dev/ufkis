# Generated by Django 3.2.15 on 2022-10-01 08:05

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background_section', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundsection',
            name='overlay_color',
            field=colorfield.fields.ColorField(blank=True, default='#FFFFFF', help_text='Этот цвет будет накладываться на изображение', image_field=None, max_length=18, null=True, samples=None, verbose_name='Цвет оверлея'),
        ),
        migrations.AddField(
            model_name='backgroundsection',
            name='overlay_opacity',
            field=models.CharField(choices=[('0', '0'), ('.1', '10%'), ('.25', '25%'), ('.5', '50%'), ('.75', '75%'), ('1', '100%')], default='.5', max_length=8, verbose_name='Прозрачность оверлея'),
        ),
        migrations.AddField(
            model_name='backgroundsection',
            name='use_overlay',
            field=models.BooleanField(default=True, verbose_name='Использовать оверлей'),
        ),
    ]