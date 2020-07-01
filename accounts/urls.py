from django.urls import path, re_path, include
from rest_framework import routers
from . import viewsets
from . import views

router = routers.DefaultRouter()
router.register(r'follows', viewsets.FollowViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<username>', views.profile, name='profiledetail'),
    path('edit/', views.editprofile, name='editprofile'),
    re_path(r'^follow/(?P<id>[\w-]+)/$', views.follow, name='follow'),
    re_path(r'^unfollow/(?P<id>[\w-]+)/$', views.unfollow, name='unfollow'),
]