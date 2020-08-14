from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like
from stream_django.activity import Activity
from autoslug import AutoSlugField
from django.urls import reverse
from tinymce import HTMLField
import tagulous.models
import gdpr_assist


class Question(models.Model, Activity):
    title = models.CharField(max_length=255, verbose_name='Tytuł', help_text='')
    body = HTMLField(verbose_name='Treść')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    votes = GenericRelation(Like, related_query_name='questionlikes')
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title
    
    @property
    def activity_actor_attr(self):
        return self.author

    def get_absolute_url(self):
        return reverse('questiondetail', args=[self.slug])

class Answer(models.Model, Activity):
    body = models.TextField(verbose_name='Treść')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    votes = GenericRelation(Like, related_query_name='answerlikes')

    def __str__(self):
        return self.body

    @property
    def activity_actor_attr(self):
        return self.author