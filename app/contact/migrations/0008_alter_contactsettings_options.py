# Generated by Django 4.2.3 on 2023-08-17 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_remove_contactsettings_recipient_emails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactsettings',
            options={'verbose_name': 'Конфигурация виртуальной приемной'},
        ),
    ]
