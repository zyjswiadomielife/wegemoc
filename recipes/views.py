from django.shortcuts import render, get_object_or_404, redirect
from .models import RecipeCategory, Embed
from django.http import HttpResponse
from django.views.generic import ListView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from comments.forms import CommentFormRecipe
from comments.models import CommentRecipe
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse
from wegemoc.settings import IFRAMELYKEY
from django.db.models import Count
from dal import autocomplete


import requests
import json

from .forms import SubmitEmbed, EmbedEdit, AddCategory
from .serializer import EmbedSerializer

@login_required
def save_embed(request):
    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            r = requests.get('http://iframe.ly/api/oembed?url='+ url + '&api_key=' + IFRAMELYKEY)
            json = r.json()
            serializer = EmbedSerializer(data=json, context={'request': request})
            if serializer.is_valid():
                embed = serializer.save()
                redir_url = reverse(
                "embededit",
                kwargs={"pk": embed.id})
                return redirect(redir_url)
    else:
        form = SubmitEmbed()

    return render(request, 'embed/embedadd.html', {'form': form})

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

@login_required
def addcategory(request):

    if request.method == 'POST':
        form = AddCategory(request.POST, request.FILES)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.author = request.user
            new_category.save()
            new_category.subscribers.add(request.user)
            return redirect('category', slug=new_category.slug)
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

def subscribe(request, recipecategory):

    recipecategory = get_object_or_404(RecipeCategory, slug=recipecategory)

    user = request.user
    if recipecategory in user.subscribed_category.all():
        recipecategory.subscribers.remove(user)
    else:
        recipecategory.subscribers.add(user)
    return HttpResponse(recipecategory.subscribers.count())

@login_required
def feed(request):
    user = get_object_or_404(User, username=request.user)
    categories = user.subscribed_category.prefetch_related('embeds')
    return render(request, 'recipes/feed.html',
                {'categories': categories})