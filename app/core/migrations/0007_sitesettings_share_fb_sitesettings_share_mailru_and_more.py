# Generated by Django 4.1.7 on 2023-06-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_sitesettings_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='share_fb',
            field=models.BooleanField(default=False, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='share_mailru',
            field=models.BooleanField(default=True, verbose_name='Mail.ru'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='share_ok',
            field=models.BooleanField(default=True, verbose_name='Одноклассники'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='share_twitter',
            field=models.BooleanField(default=True, verbose_name='Twitter'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='share_vk',
            field=models.BooleanField(default=True, verbose_name='Вконтакте'),
        ),
    ]
