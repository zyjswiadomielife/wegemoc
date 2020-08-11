# Generated by Django 2.2.13 on 2020-08-11 10:37

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tagulous.models.fields
import tagulous.models.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagulous_Post_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog', verbose_name='Miniatura')),
                ('title', models.CharField(max_length=255, verbose_name='Tytuł')),
                ('body', tinymce.models.HTMLField(verbose_name='Treść')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', tagulous.models.fields.TagField(_set_tag_meta=True, help_text='Enter a comma-separated tag string', max_count=5, to='blog.Tagulous_Post_tags', verbose_name='Tagi')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
