# Generated by Django 4.2.3 on 2023-09-19 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingEventsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('num_objects', models.PositiveIntegerField(default=3, verbose_name='Количество мероприятий')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start_at'], 'verbose_name': 'мероприятие', 'verbose_name_plural': 'мероприятия'},
        ),
    ]