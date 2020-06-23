from django.urls import path, re_path, include
from rest_framework import routers
from . import views
from .views import EmbedAddView
from . import viewsets
from django.contrib.auth.models import User

router = routers.DefaultRouter()
router.register(r'embeds', viewsets.EmbedViewSet)
router.register(r'recipecategories', viewsets.RecipeCategoryViewSet)

urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipelist'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('feed/', views.feed, name='feed'),
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.addcategory, name='addcategory'),
    re_path(r'^category-autocomplete/$', views.CategoryAutocomplete.as_view(),name='category-autocomplete'),
    re_path(r'^allcategories-autocomplete/$', views.AllCategoriesAutocomplete.as_view(),name='allcategories-autocomplete'),
    path('<slug>/', views.recipedetail, name='recipedetail'),
    path('recipe/embed/add/', views.save_embed, name='addembed'),
    path('categories/suggestions/', views.suggestedcategories, name='suggestions'),
    path('recipe/embed/add1/', EmbedAddView.as_view(), name='embedadd'),
    path('embed/<int:pk>/edit/', views.EmbedUpdate.as_view(), name='embededit'),
    re_path(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),
    re_path(r'^b/(?P<recipecategory>[-\w]+)/subscription/$', views.subscribe, name='subscribe'),
    path('u/<username>/subscriptions/', views.UserSubscriptionListView.as_view(), name='user_subscription_list'),
]