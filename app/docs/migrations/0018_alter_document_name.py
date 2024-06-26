# Generated by Django 4.2.3 on 2023-08-11 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0017_remove_taggeddocument_content_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='Документ', help_text='Примеры: "Приказ Минспорта РФ" , "Уставной документ", и т.д.   Номер и дату в этом поле не указывайте', max_length=512, verbose_name='Название документа'),
        ),
    ]
