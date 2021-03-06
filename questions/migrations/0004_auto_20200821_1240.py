# Generated by Django 2.2.13 on 2020-08-21 10:40

from django.db import migrations
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20200821_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, autocomplete_settings={'width': 'resolve'}, help_text='Enter a comma-separated tag string', max_count=3, to='questions.Tagulous_Question_tags'),
        ),
    ]
