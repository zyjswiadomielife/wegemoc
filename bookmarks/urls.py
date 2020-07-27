from django.urls import re_path, path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('<id>/bookmark/', views.bookmark, name='bookmark'),
    path('<username>/bookmarks/', views.UserBookmarksListView.as_view(), name='user_bookmarks_list'),
]