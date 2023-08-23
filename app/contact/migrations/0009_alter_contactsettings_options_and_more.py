# Generated by Django 4.2.3 on 2023-08-20 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_alter_contactsettings_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactsettings',
            options={'verbose_name': 'Конфигурация виртуальной приемной', 'verbose_name_plural': 'Конфигурация виртуальной приемной'},
        ),
        migrations.AlterField(
            model_name='contactsettings',
            name='userdata_checkbox_text',
            field=models.CharField(default='Я соглашаюсь на обработку моих персональных данных', max_length=256, verbose_name='Текст галочки на форме данных пользователя'),
        ),
    ]