from rest_framework import viewsets, generics
from .serializer import EmbedSerializer, RecipeCategorySerializer, UserSerializer
from .models import Embed, RecipeCategory
from django.contrib.auth.models import User
from mptt.templatetags.mptt_tags import cache_tree_children
from rest_framework.response import Response

class EmbedViewSet(viewsets.ModelViewSet):

    queryset = Embed.objects.all()
    serializer_class = EmbedSerializer

class RecipeCategoryViewSet(viewsets.ModelViewSet):
    
    def list(self, request):
        tree = cache_tree_children(RecipeCategory.objects.filter(level=0))
        serializer_class = RecipeCategorySerializer(tree, many=True)
        return Response(serializer_class.data)

class Suggestions(generics.ListAPIView):

    serializer_class = RecipeCategorySerializer

    def get_queryset(self):
        user = self.request.user
        return user.subscribed_category.prefetch_related('embeds')