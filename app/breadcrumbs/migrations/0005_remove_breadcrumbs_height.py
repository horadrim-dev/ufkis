# Generated by Django 4.1.7 on 2023-06-08 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breadcrumbs', '0004_remove_breadcrumbs_shadow_breadcrumbs_white_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breadcrumbs',
            name='height',
        ),
    ]
