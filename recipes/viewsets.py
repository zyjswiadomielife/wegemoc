from rest_framework import viewsets
from .serializer import EmbedSerializer, RecipeCategorySerializer
from .models import Embed, RecipeCategory

class EmbedViewSet(viewsets.ModelViewSet):

    queryset = Embed.objects.all()
    serializer_class = EmbedSerializer

class RecipeCategoryViewSet(viewsets.ModelViewSet):

    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeCategorySerializer