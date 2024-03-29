# Generated by Django 4.1.7 on 2023-03-16 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background_section', '0011_backgroundsection_padding_bottom_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backgroundsection',
            name='text',
        ),
        migrations.RemoveField(
            model_name='backgroundsection',
            name='text_bottom',
        ),
        migrations.AddField(
            model_name='backgroundsection',
            name='name',
            field=models.CharField(default='', help_text='Системное название секции (отображается только в панели администрирования)', max_length=255, verbose_name='Название'),
        ),
    ]
