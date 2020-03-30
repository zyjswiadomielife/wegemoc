from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.questionlist, name='questionlist'),
    path('<slug>', views.questiondetail, name='questiondetail'),
    path('add/', views.questionadd, name='questionadd'),
]