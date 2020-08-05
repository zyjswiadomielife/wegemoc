"""wegemoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from recipes.models import Embed
from home.views import home

sitemaps = {
    'recipes': GenericSitemap({
        'queryset': Embed.objects.all(),
        'date_field': 'created_at',
    }, priority=0.9),
}

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('forum/', include('questions.urls')),
    path('recipes/', include('recipes.urls')),
    path('blog/', include('blog.urls')),
    path('account/', include('accounts.urls')),
    path('like/', include('likes.urls')),
    path('bookmarks/', include('bookmarks.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r"^messages/", include("pinax.messages.urls", namespace="pinax_messages")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('sentry-debug/', trigger_error),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)