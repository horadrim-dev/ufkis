# Generated by Django 4.2.3 on 2023-10-03 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_button_text_event_use_button'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='event',
            name='use_button',
        ),
    ]