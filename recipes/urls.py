from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipelist'),
    path('feed/', views.feed, name='feed'),
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.addcategory, name='addcategory'),
    re_path(r'^category-autocomplete/$', views.CategoryAutocomplete.as_view(),name='category-autocomplete'),
    path('<slug>/', views.recipedetail, name='recipedetail'),
    path('recipe/embed/add/', views.save_embed, name='addembed'),
    path('embed/<int:pk>/edit/', views.EmbedUpdate.as_view(), name='embededit'),
    re_path(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),
    re_path(r'^b/(?P<recipecategory>[-\w]+)/subscription/$', views.subscribe, name='subscribe'),
    path('u/<username>/subscriptions/', views.UserSubscriptionListView.as_view(), name='user_subscription_list'),
]