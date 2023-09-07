# Generated by Django 4.2.3 on 2023-09-06 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('docs', '0033_alter_documentsplugin_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentsplugin',
            name='tags',
        ),
        migrations.AddField(
            model_name='documentsplugin',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taggit.tag'),
        ),
    ]
