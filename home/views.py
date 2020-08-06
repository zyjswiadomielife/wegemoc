from django.shortcuts import render
from recipes.models import Embed, RecipeCategory
from django.views.generic import TemplateView

def home(request):
    embeds = Embed.objects.all()
    categories = RecipeCategory.objects.filter(level=1).order_by('-subscribers')
    return render(request, 'recipes/embed_home.html', {'embeds': embeds,
                                                    'categories': categories})


class RegulaminView(TemplateView):
    template_name = "tos/regulamin.html"

class PolitykaprywatnosciView(TemplateView):
    template_name = "tos/polityka.html"

def choose_category(request):
    rootcategories = RecipeCategory.objects.root_nodes().filter(level=0)
    subcats = RecipeCategory.objects.filter(level=1)
    print(subcats)

    return render(request, 'steps/categories.html', {'rootcategories':rootcategories,
                                                    'subcats': subcats})
