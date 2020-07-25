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

    def validate(self, attrs):
        url = attrs['thumbnail_url']
        data = requests.get(url)
        response = requests.get(attrs['thumbnail_url'])
        random_name = uuid.uuid4().hex + ".jpg"
        folder_name = "recipes"
        absolute_file_path = os.path.join(settings.MEDIA_ROOT, folder_name, random_name)
        relative_path = os.path.join(folder_name, random_name)
        with open(absolute_file_path, 'wb') as f:
            f.write(response.content)
        attrs['image'] = relative_path
        return attrs


class RecipeCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeCategory
        fields = '__all__'
    

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'