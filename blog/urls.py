from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.postlist, name='postlist'),
    path('<slug>', views.postdetail, name='postdetail'),
]