# Generated by Django 4.2.3 on 2023-08-30 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0019_organization_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='description',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='short_description',
        ),
    ]
