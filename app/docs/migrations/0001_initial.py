# Generated by Django 4.2.3 on 2023-08-09 06:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0015_alter_file_owner_alter_file_polymorphic_ctype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(blank=True, default=0, help_text='Если оставить равным 0 - добавится в конец.', null=True, verbose_name='Порядок')),
                ('name', models.CharField(max_length=64, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(blank=True, default=0, help_text='Если оставить равным 0 - добавится в конец.', null=True, verbose_name='Порядок')),
                ('name', models.CharField(help_text='Распоряжение, постановление, приказ и т.д.', max_length=64, verbose_name='Название типа документа')),
            ],
            options={
                'verbose_name': 'тип документа',
                'verbose_name_plural': 'типы документов',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата')),
                ('number', models.CharField(blank=True, max_length=32, null=True, verbose_name='Номер')),
                ('name', models.CharField(blank=True, max_length=512, null=True, verbose_name='Название')),
                ('document_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на документ')),
                ('published_at', models.DateField(default=datetime.date.today, verbose_name='Дата публикации')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.category')),
                ('document_file', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.file', verbose_name='Файл документа')),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.documenttype')),
            ],
            options={
                'verbose_name': 'документ',
                'verbose_name_plural': 'документы',
                'ordering': ['-published_at'],
            },
        ),
    ]
