# Generated by Django 4.2.3 on 2023-09-21 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_purecodeplugin_css_purecodeplugin_js'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purecodeplugin',
            name='code',
            field=models.TextField(blank=True, help_text='Использовать js и css здесь возможно, но не рекомендуется.', null=True, verbose_name='HTML'),
        ),
        migrations.AlterField(
            model_name='purecodeplugin',
            name='js',
            field=models.TextField(blank=True, help_text='Доступно использование jQuery, пример "$(document).ready(function () {                           alert("test");});"', null=True, verbose_name='JAVASCRIPT'),
        ),
    ]