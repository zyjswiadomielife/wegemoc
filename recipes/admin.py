from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import RecipeCategory, Embed

admin.site.register(Embed)
admin.site.register(RecipeCategory, MPTTModelAdmin)