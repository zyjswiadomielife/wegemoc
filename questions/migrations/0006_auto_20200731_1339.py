# Generated by Django 2.2.13 on 2020-07-31 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20200730_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.TextField(verbose_name='Treść'),
        ),
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(verbose_name='Treść'),
        ),
    ]