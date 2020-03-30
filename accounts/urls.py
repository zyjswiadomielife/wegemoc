from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<username>', views.profile, name='profiledetail'),
    re_path(r'^follow/(?P<id>[\w-]+)/$', views.follow, name='follow'),
    re_path(r'^unfollow/(?P<id>[\w-]+)/$', views.unfollow, name='unfollow'),
]