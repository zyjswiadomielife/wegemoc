from django.urls import path, re_path, include
from rest_framework import routers
from . import views
from .views import EmbedAddView
from . import viewsets
from .models import RecipeCategory, Embed
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from home.views import choose_category

router = routers.DefaultRouter()
router.register(r'embeds', viewsets.EmbedViewSet)
router.register(r'recipecategories', viewsets.RecipeCategoryViewSet, basename="RecipeCategory")

urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipelist'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('suggestions/', viewsets.Suggestions.as_view(), name='suggestions'),
    path('feed/', views.feed, name='feed'),
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.addcategory, name='addcategory'),
    path('<slug>/', views.recipedetail, name='recipedetail'),
    path('recipe/embed/add/', login_required(views.EmbedAddView.as_view()), name='embedadd'),
    path('embed/<int:pk>/edit/', views.EmbedUpdate.as_view(), name='embededit'),
    re_path(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),
    path('<recipecategory>/subscriptionadd/', views.subscribeadd, name='subscribeadd'),
    path('<recipecategory>/subscriptiondelete/', views.subscribedelete, name='subscribedelete'),
    path('u/<username>/subscriptions/', views.UserSubscriptionListView.as_view(), name='user_subscription_list'),
    path('steps/choose/', choose_category, name='choosecategory'),
]