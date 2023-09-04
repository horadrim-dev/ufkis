# Generated by Django 4.2.3 on 2023-09-01 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_headerplugin_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headerplugin',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='headerplugin',
            name='title',
        ),
        migrations.AddField(
            model_name='headerplugin',
            name='size',
            field=models.CharField(choices=[('medium', 'Средне'), ('small', 'Чуть чуть'), ('large', 'Побольше')], default='medium', verbose_name='Размер'),
        ),
    ]