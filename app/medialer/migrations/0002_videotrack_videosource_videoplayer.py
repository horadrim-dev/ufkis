# Generated by Django 4.1.7 on 2023-06-21 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('filer', '0015_alter_file_owner_alter_file_polymorphic_ctype_and_more'),
        ('medialer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoTrack',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('kind', models.CharField(choices=[('subtitles', 'Subtitles'), ('captions', 'Captions'), ('descriptions', 'Descriptions'), ('chapters', 'Chapters')], max_length=255, verbose_name='Kind')),
                ('srclang', models.CharField(blank=True, help_text='Examples: "en" or "de" etc.', max_length=255, verbose_name='Source language')),
                ('label', models.CharField(blank=True, max_length=255, verbose_name='Label')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('src', filer.fields.file.FilerFileField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.file', verbose_name='Source file')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='VideoSource',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('text_title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('text_description', models.TextField(blank=True, verbose_name='Description')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('source_file', filer.fields.file.FilerFileField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='filer.file', verbose_name='Source')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='VideoPlayer',
            fields=[
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('label', models.CharField(blank=True, max_length=255, verbose_name='Label')),
                ('embed_link', models.CharField(blank=True, help_text='Use this field to embed videos from external services such as YouTube, Vimeo or others. Leave it blank to upload video files by adding nested "Source" plugins.', max_length=255, verbose_name='Embed link')),
                ('parameters', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, help_text='Parameters are appended to the video link if provided.', verbose_name='Parameters')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('poster', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='Poster')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
