# Generated by Django 4.2.3 on 2023-08-05 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0013_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='sotrudnik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='structure.sotrudnik'),
        ),
    ]