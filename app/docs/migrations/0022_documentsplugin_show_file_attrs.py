# Generated by Django 4.2.3 on 2023-08-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0021_documentsplugin_show_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentsplugin',
            name='show_file_attrs',
            field=models.BooleanField(default=True, verbose_name='Отображать атрибуты файла'),
        ),
    ]
