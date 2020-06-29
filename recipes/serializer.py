from rest_framework import serializers
from .models import Embed, RecipeCategory
from django.contrib.auth.models import User
import os, uuid, requests
from django.conf import settings
from django.db.models import Count



class EmbedSerializer(serializers.ModelSerializer):
    added_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Embed
        fields = '__all__'

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

class RecursiveField(serializers.Serializer):

    def to_native(self, value):
        return RecipeCategorySerializer(value, context={"parent": self.parent.object, "parent_serializer": self.parent})

class RecipeCategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, required=False)
    full_name = serializers.SerializerMethodField("get_full_name")

    class Meta:
        model = RecipeCategory
        fields = '__all__'
    
    def get_full_name(self, obj):
        name = obj.title

        if "parent" in self.context:
            parent = self.context["parent"]

            parent_name = self.context["parent_serializer"].get_full_name(parent)

            name = "%s - %s" % (parent_name, name, )

        return name

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'