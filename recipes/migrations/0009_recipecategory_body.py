# Generated by Django 2.1.5 on 2019-04-17 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20190417_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipecategory',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
