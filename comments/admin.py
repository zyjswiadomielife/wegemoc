from django.contrib import admin
from .models import CommentPost, CommentRecipe

admin.site.register(CommentPost)
admin.site.register(CommentRecipe)