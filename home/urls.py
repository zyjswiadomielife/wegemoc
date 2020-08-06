from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('regulamin/', views.RegulaminView.as_view(), name='regulamin'),
    path('polityka-prywatnosci/', views.PolitykaprywatnosciView.as_view(), name='polityka'),
]