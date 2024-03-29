# Generated by Django 4.2.3 on 2023-08-15 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactsettings_agreement_checkbox_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactsettings',
            name='agreement_title',
            field=models.CharField(default='Прочитайте правила пользования виртуальной приемной', max_length=256, verbose_name='Название этапа ознакомления с соглашением'),
        ),
        migrations.AddField(
            model_name='contactsettings',
            name='message_title',
            field=models.CharField(default='Заполните и отправьте обращение', max_length=256, verbose_name='Название этапа заполнения обращение'),
        ),
        migrations.AddField(
            model_name='contactsettings',
            name='userdata_title',
            field=models.CharField(default='Укажите данные о себе', max_length=256, verbose_name='Название этапа ввода пользовательских данных'),
        ),
    ]
