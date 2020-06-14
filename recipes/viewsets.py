from rest_framework import viewsets
from .serializer import EmbedSerializer
from .models import Embed

class EmbedViewSet(viewsets.ModelViewSet):

    queryset = Embed.objects.all()
    serializer_class = EmbedSerializer