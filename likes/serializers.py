from rest_framework import serializers
from .models import Like
from django.contrib.auth.models import User
from django.db.models import Count
from recipes.models import Embed



class LikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total_votes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'

    def get_total_votes(self, embed):
        return embed.content_object.votes.count()
