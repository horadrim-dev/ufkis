# Generated by Django 4.2.3 on 2023-10-07 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_alter_dayevent_options_alter_event_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayevent',
            name='place',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Место проведения'),
        ),
    ]