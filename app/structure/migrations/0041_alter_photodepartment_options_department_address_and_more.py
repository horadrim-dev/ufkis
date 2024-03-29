# Generated by Django 4.2.3 on 2023-09-14 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0040_photodepartment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photodepartment',
            options={'verbose_name': 'фото', 'verbose_name_plural': 'фото'},
        ),
        migrations.AddField(
            model_name='department',
            name='address',
            field=models.CharField(blank=True, help_text='Заполняется если адрес секции не совпадает с адресом организации', max_length=512, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='department',
            name='address_same',
            field=models.BooleanField(default=True, verbose_name='Адрес совпадает с адресом организации'),
        ),
    ]
