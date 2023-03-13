# Generated by Django 3.2.15 on 2022-10-26 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0010_attraction_placeholder_bottom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attraction',
            name='price_card',
        ),
        migrations.RemoveField(
            model_name='attraction',
            name='price_nocard',
        ),
        migrations.RemoveField(
            model_name='attraction',
            name='short_description',
        ),
        migrations.AddField(
            model_name='attraction',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена, руб/билет'),
        ),
        migrations.AddField(
            model_name='attraction',
            name='rental_time',
            field=models.FloatField(default=0, help_text='(0 = без ограничений)', verbose_name='Время проката, в минутах'),
        ),
        migrations.AddField(
            model_name='attraction',
            name='restrictions',
            field=models.CharField(default='', max_length=1024, verbose_name='Ограничения'),
        ),
    ]
