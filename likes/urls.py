from django.urls import re_path, path, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from recipes.models import Embed
from . import viewsets
from . import views

router = routers.DefaultRouter()
router.register(r'likes', viewsets.LikeViewSet)

app_name = 'ajax'
urlpatterns = [
    path('', include(router.urls)),
    path('embed/<pk>/', login_required(views.VotesView.as_view(model=Embed)), name='embed_like'),
    path('question/<pk>/', login_required(views.VotesView.as_view(model=Embed)), name='embed_like'),
    path('answer/<pk>/', login_required(views.VotesView.as_view(model=Embed)), name='embed_like'),
]