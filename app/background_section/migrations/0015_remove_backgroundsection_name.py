# Generated by Django 4.1.7 on 2023-07-03 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('background_section', '0014_alter_backgroundsection_overlay_opacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backgroundsection',
            name='name',
        ),
    ]
