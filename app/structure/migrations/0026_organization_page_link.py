# Generated by Django 4.2.3 on 2023-09-01 03:31

import cms.models.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('structure', '0025_sotrudnikorganizationplugin_apparat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='page_link',
            field=cms.models.fields.PageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.page'),
        ),
    ]
