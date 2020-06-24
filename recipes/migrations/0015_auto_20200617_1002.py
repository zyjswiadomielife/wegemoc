# Generated by Django 2.2.13 on 2020-06-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_auto_20191214_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embed',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='embed',
            name='url',
            field=models.URLField(max_length=255, verbose_name='Adres przepisu'),
        ),
    ]