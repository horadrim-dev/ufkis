# Generated by Django 4.2.3 on 2023-08-20 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('core', '0013_sitesettings_menu_style_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='extended_fields', to='cms.page', verbose_name='Page')),
            ],
        ),
    ]
