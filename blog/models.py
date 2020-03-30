from django.db import models
from tinymce import HTMLField
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.urls import reverse
import tagulous.models

class Post(models.Model):
    image = models.ImageField(upload_to='blog', verbose_name='Miniatura')
    title = models.CharField(max_length=255, verbose_name='Tytuł')
    body = HTMLField(verbose_name='Treść')
    created_at = models.DateTimeField(auto_now_add=True)
    tags = tagulous.models.TagField(max_count=5, verbose_name='Tagi')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('postdetail', args=[self.slug])