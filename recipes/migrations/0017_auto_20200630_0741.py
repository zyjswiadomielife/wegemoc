# Generated by Django 2.2.12 on 2020-06-30 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_recipecategory_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipecategory',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Pełna nazwa'),
        ),
    ]
