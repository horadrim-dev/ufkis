# Generated by Django 4.1.7 on 2023-06-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breadcrumbs', '0003_breadcrumbs_shadow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breadcrumbs',
            name='shadow',
        ),
        migrations.AddField(
            model_name='breadcrumbs',
            name='white_mode',
            field=models.BooleanField(default=False, verbose_name='Текст белым цветом'),
        ),
    ]
