from django.shortcuts import render, get_object_or_404, redirect
from .models import RecipeCategory, Embed
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, TemplateView, View
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from comments.forms import CommentFormRecipe
from comments.models import CommentRecipe
from .forms import AddEmbed
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse
from wegemoc.settings import IFRAMELYKEY
from django.db.models import Count
from dal import autocomplete



import requests
import json

from .forms import SubmitEmbed, EmbedEdit, AddCategory
from .serializer import EmbedSerializer


class EmbedAddView(TemplateView):
    template_name = "embed/addembed.html"


class EmbedUpdate(UpdateView):

    template_name_suffix = '_update_form'
    form_class = EmbedEdit
    model = Embed

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

class UserSubscriptionListView(LoginRequiredMixin, ListView):

    model = RecipeCategory
    paginate_by = 15
    template_name = 'recipes/user_subscription_list.html'
    context_object_name = 'subscriptions'

    def get_queryset(self, **kwargs):
        user = get_object_or_404(User, username=self.request.user)
        return user.subscribed_category.all()

class RecipeList(ListView):

    model = Embed
    paginate_by = 30

def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    parent = None
    root = RecipeCategory.objects.all()

    for slug in category_slug[:-1]:
        parent = root.get(parent=parent, slug = slug)

    try:
        instance = RecipeCategory.objects.get(parent=parent,slug=category_slug[-1])
    except:
        instance = get_object_or_404(Embed, slug = category_slug[-1])
        return render(request, "recipes/detail.html", {'instance':instance})
    else:
        return render(request, 'recipes/categories.html', {'instance':instance})

def categories(request):
    rootcategories = RecipeCategory.objects.root_nodes().filter(level=0)
    categories = RecipeCategory.objects.filter(level=1)
    return render(request, 'recipes/category_list.html',
                {'rootcategories': rootcategories,
                'categories': categories})


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = RecipeCategory.objects.root_nodes().filter(level=0)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class AllCategoriesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = RecipeCategory.objects.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)

        return qs

@login_required
def addcategory(request):

    if request.method == 'POST':
        form = AddCategory(request.POST, request.FILES)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.author = request.user
            new_category.save()
            new_category.subscribers.add(request.user)
            parent = form.cleaned_data['parent']
            if parent.id == 1:
                category_html = '/recipes/category/' + 'weganskie' + '/' + new_category.slug + '/'
            else:
                category_html = '/recipes/category/' + 'wegetarianskie' + '/' + new_category.slug + '/'
            return HttpResponseRedirect(category_html)
    else:
        form = AddCategory()
    return render(request, 'recipes/add.html', {'form': form})


def recipedetail(request, slug):
    recipe = get_object_or_404(Embed, slug=slug)
    categories = RecipeCategory.objects.all()
    recipe_category_ids = recipe.category.values_list('id', flat=True)
    similar_posts = Embed.objects.filter(category__in=recipe_category_ids).exclude(id=recipe.id)
    similar_posts = similar_posts.annotate(same_category=Count('category')).order_by('-same_category', '-created_at')[:6]
    comments = recipe.recipecomments.all()
    num_embed = Embed.objects.filter(added_by=recipe.added_by).count()

    if request.method == 'POST':
        form = CommentFormRecipe(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.recipe = recipe
            new_comment.save()
    else:
        form = CommentFormRecipe()

    return render(request, 'recipes/detail.html', {'recipe': recipe,
                                                  'categories': categories,
                                                  'similar_posts': similar_posts,
                                                  'comments': comments,
                                                  'form': form,
                                                  'num_embed': num_embed})

def subscribeadd(request, recipecategory):

    recipecategory = get_object_or_404(RecipeCategory, slug=recipecategory)

    user = request.user
    if recipecategory not in user.subscribed_category.all():
        recipecategory.subscribers.add(user)
    return HttpResponse(
            json.dumps({
                "subscribers_count": recipecategory.subscribers.count(),
            }),
            content_type="application/json"
        )

def subscribedelete(request, recipecategory):

    recipecategory = get_object_or_404(RecipeCategory, slug=recipecategory)

    user = request.user
    if recipecategory in user.subscribed_category.all():
        recipecategory.subscribers.remove(user)
        
    return HttpResponse(
            json.dumps({
                "subscribers_count": recipecategory.subscribers.count(),
            }),
            content_type="application/json"
        )

@login_required
def feed(request):
    user = get_object_or_404(User, username=request.user)
    categories = user.subscribed_category.prefetch_related('embeds')
    return render(request, 'recipes/feed.html',
                {'categories': categories})

