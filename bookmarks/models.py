from django.db import models
from django.contrib.auth.models import User
from recipes.models import Embed


class Bookmark(models.Model):
    obj = models.ForeignKey(Embed, on_delete=models.CASCADE, related_name='bookmarks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userbookmarks')
    created_at = models.DateTimeField(auto_now_add=True)


