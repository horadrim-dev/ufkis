# Generated by Django 4.1.7 on 2023-05-31 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_remove_post_text_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_position',
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]