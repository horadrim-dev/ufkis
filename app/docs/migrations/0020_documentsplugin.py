# Generated by Django 4.2.3 on 2023-08-12 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('docs', '0019_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
