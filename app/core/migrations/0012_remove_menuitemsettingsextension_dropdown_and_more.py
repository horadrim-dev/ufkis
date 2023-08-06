# Generated by Django 4.2.3 on 2023-08-06 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_menuitemsettingsextension_dropdown'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitemsettingsextension',
            name='dropdown',
        ),
        migrations.AddField(
            model_name='menuitemsettingsextension',
            name='dropdown_mega',
            field=models.BooleanField(default=False, verbose_name='Стиль выпадающего меню'),
        ),
    ]
