# Generated by Django 4.1.7 on 2023-02-20 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='IconExtension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fa_icon', models.TextField(default='')),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.page')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='core.iconextension')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
