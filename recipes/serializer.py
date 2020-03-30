from rest_framework import serializers
from .models import Embed
import os, uuid, requests
from django.conf import settings

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