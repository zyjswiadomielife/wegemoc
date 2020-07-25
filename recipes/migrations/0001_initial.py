# Generated by Django 2.2.13 on 2020-07-25 08:55

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import stream_django.activity


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Nazwa kategorii')),
                ('parentname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Pełna nazwa')),
                ('body', models.TextField(blank=True, help_text='To pole nie jest obowiązkowe. Jeśli chcesz, możesz napisać co konkretnie ma być dodawane do tej kategorii.', verbose_name='Opis kategorii')),
                ('image', models.ImageField(blank=True, default='defaultbgcategory.jpg', help_text='Dodając zdjęcie jesteś w stanie wyróżnić kategorię, jeśli jednak tego nie zrobisz nic się nie stanie. :)', null=True, upload_to='Tło', verbose_name='Tło kategorii')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='recipes.RecipeCategory', verbose_name='Kategoria')),
                ('subscribers', models.ManyToManyField(blank=True, related_name='subscribed_category', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Kategorie',
                'unique_together': {('parent', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Embed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255, verbose_name='Adres przepisu')),
                ('title', models.CharField(max_length=255, verbose_name='Tytuł')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Opis')),
                ('type', models.CharField(blank=True, max_length=200)),
                ('thumbnail_url', models.URLField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, upload_to='recipes')),
                ('html', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addedbyuser', to=settings.AUTH_USER_MODEL)),
                ('category', mptt.fields.TreeManyToManyField(blank=True, null=True, related_name='embeds', to='recipes.RecipeCategory', verbose_name='Kategoria')),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=(models.Model, stream_django.activity.Activity),
        ),
    ]
