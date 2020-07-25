from django.urls import re_path, path
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
router.register(r'likes', viewsets.LikeViewSet)

app_name = 'ajax'
urlpatterns = [

]