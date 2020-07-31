# Generated by Django 2.2.13 on 2020-07-30 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gdpr_assist


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='anonymised',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='anonymised',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=gdpr_assist.ANONYMISE(django.db.models.deletion.SET_NULL), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=gdpr_assist.ANONYMISE(django.db.models.deletion.SET_NULL), to=settings.AUTH_USER_MODEL),
        ),
    ]