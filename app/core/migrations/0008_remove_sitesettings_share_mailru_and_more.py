# Generated by Django 4.1.7 on 2023-06-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_sitesettings_share_fb_sitesettings_share_mailru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='share_mailru',
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='share_instagram',
            field=models.BooleanField(default=False, verbose_name='Instagram'),
        ),
    ]
