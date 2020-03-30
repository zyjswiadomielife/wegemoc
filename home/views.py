from django.shortcuts import render
from recipes.models import Embed, RecipeCategory
from django.views.generic import ListView

def home(request):
    embeds = Embed.objects.all()
    categories = RecipeCategory.objects.filter(level=1).order_by('-subscribers')
    return render(request, 'recipes/embed_home.html', {'embeds': embeds,
                                                    'categories': categories})