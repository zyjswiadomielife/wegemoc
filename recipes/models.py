from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from django.contrib.contenttypes.fields import GenericRelation
from tinymce import HTMLField
from django.urls import reverse
from likedislike.models import LikeDislike
from stream_django.activity import Activity
from django.core.files import File
from urllib import request
import os

class RecipeCategory(MPTTModel):
    title = models.CharField(max_length=255, verbose_name='Nazwa kategorii')
    body = models.TextField(verbose_name='Opis kategorii', blank=True, help_text='To pole nie jest obowiązkowe. Jeśli chcesz, możesz napisać co konkretnie ma być dodawane do tej kategorii.')
    image = models.ImageField(upload_to='Tło', default='defaultbgcategory.jpg' ,verbose_name='Tło kategorii', help_text='Dodając zdjęcie jesteś w stanie wyróżnić kategorię, jeśli jednak tego nie zrobisz nic się nie stanie. :)', null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    parent = TreeForeignKey('self', related_name='children', db_index=True, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Kategoria')
    subscribers = models.ManyToManyField(User, related_name='subscribed_category', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'Kategorie'

    def get_slug_list(self):

        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [ i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))
        return slugs


class Embed(models.Model, Activity):
    url = models.URLField(max_length=255, verbose_name='Adres przepisu')
    title = models.CharField(max_length=255, verbose_name='Tytuł')
    description = HTMLField(verbose_name='Opis', blank=True, null=True)
    type = models.CharField(blank=True, max_length=200)
    thumbnail_url = models.URLField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='recipes', blank=True)
    html = models.TextField()
    votes = GenericRelation(LikeDislike, related_query_name='embedlikes')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = TreeManyToManyField(RecipeCategory, blank=True, null=True, related_name='embeds', verbose_name='Kategoria')
    slug = AutoSlugField(populate_from='title', unique=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('recipedetail',
                       args=[self.slug])

    @property
    def activity_actor_attr(self):
        return self.added_by
