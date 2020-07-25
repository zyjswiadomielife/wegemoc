from rest_framework import serializers
from .models import Like
from django.contrib.auth.models import User
from django.db.models import Count



class LikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total_votes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'

    def get_total_votes(self, like):
        return like.content_object.count()
