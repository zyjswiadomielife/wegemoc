from django.forms import ModelForm
from django import forms
from .models import CommentPost, CommentRecipe

class CommentFormPost(ModelForm):

    class Meta:
        model = CommentPost
        fields = ['body']


class CommentFormRecipe(ModelForm):

    class Meta:
        model = CommentRecipe
        fields = ['body']