# Generated by Django 4.1.7 on 2023-06-22 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medialer', '0002_videotrack_videosource_videoplayer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'альбом',
                'verbose_name_plural': 'альбомы',
            },
        ),
    ]
