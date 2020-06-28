from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class EditUser(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

class EditProfile(ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'url', 'facebook']
