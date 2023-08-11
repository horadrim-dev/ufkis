# Generated by Django 4.2.3 on 2023-08-11 06:04

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('docs', '0016_tag_taggeddocument_document_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggeddocument',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='taggeddocument',
            name='tag',
        ),
        migrations.AlterField(
            model_name='document',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='TaggedDocument',
        ),
    ]