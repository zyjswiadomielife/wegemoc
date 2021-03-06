# Generated by Django 2.2.13 on 2020-08-17 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stream_django.activity


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='defaultavatar.png', upload_to='avatar', verbose_name='Awatar profilu')),
                ('bio', models.TextField(blank=True, verbose_name='O mnie')),
                ('url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Link do bloga lub innej strony')),
                ('facebook', models.URLField(blank=True, max_length=255, null=True, verbose_name='Profil lub fanpage na Facebooku')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'target')},
            },
            bases=(stream_django.activity.Activity, models.Model),
        ),
    ]
