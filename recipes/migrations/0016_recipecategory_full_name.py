# Generated by Django 2.2.12 on 2020-06-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_auto_20200617_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipecategory',
            name='full_name',
            field=models.CharField(default=1, max_length=255, verbose_name='Pełna nazwa'),
            preserve_default=False,
        ),
    ]
