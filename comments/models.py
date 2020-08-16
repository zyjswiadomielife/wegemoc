from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from recipes.models import Embed
from stream_django.activity import Activity

class Comment(models.Model, Activity):
    body = models.TextField(verbose_name='Treść komentarza')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    @property
    def activity_actor_attr(self):
        return self.author

class CommentPost(Comment):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postcomments')

class CommentRecipe(Comment):
    recipe = models.ForeignKey(Embed, on_delete=models.CASCADE, related_name='recipecomments')