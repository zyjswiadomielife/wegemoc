from rest_framework import serializers
from .models import Embed, RecipeCategory
from django.contrib.auth.models import User
import os, uuid, requests
from django.conf import settings
from django.db.models import Count



class EmbedSerializer(serializers.ModelSerializer):
    added_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total_votes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Embed
        fields = '__all__'

    def get_total_votes(self, embed):
        return embed.votes.count()



class RecipeCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeCategory
        fields = '__all__'
    

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'