# Generated by Django 4.2.3 on 2023-08-22 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0028_documentplugin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='DocumentCategory',
        ),
    ]