# Generated by Django 4.1.7 on 2023-07-18 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0009_organization_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='short_description',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Краткое описание'),
        ),
    ]
