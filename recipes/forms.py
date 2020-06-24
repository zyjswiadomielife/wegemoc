from django.forms import ModelForm, ModelChoiceField
from django import forms
from mptt.forms import TreeNodeChoiceField, TreeNodeMultipleChoiceField
from .models import RecipeCategory, Embed
from dal import autocomplete

class AddEmbed(ModelForm):

    url = forms.URLField(label='Adres przepisu', widget=forms.URLInput(attrs={'v-model': 'embed.url', '@paste':'paste', '@input':'input'}))
    title = forms.CharField(widget=forms.HiddenInput(attrs={':value':'embedsinfo.title'}))
    description = forms.CharField(widget=forms.HiddenInput(attrs={':value':'embedsinfo.description'}))
    thumbnail_url = forms.CharField(widget=forms.HiddenInput(attrs={':value':'embedsinfo.thumbnail_url'}))
    html = forms.CharField(widget=forms.HiddenInput(attrs={':value':'embedsinfo.html'}))
    category = forms.CharField(widget=forms.HiddenInput(attrs={':value': 'selectedId'}))

    class Meta:
        model = Embed
        fields = ['url','title', 'description', 'thumbnail_url', 'html', 'category']

class SubmitEmbed(forms.Form):
    url = forms.URLField(label='Adres przepisu', widget=forms.URLInput(attrs={'v-model': 'url'}))

class EmbedEdit(ModelForm):

    class Meta:
        category = TreeNodeMultipleChoiceField(queryset=RecipeCategory.objects.all())

        model=Embed
        fields = ['category', 'title', 'description']

class AddCategory(ModelForm):

    class Meta:
        model = RecipeCategory
        fields = ['image', 'title', 'body', 'parent']
        widgets = {
            'parent': autocomplete.ModelSelect2(url='category-autocomplete')
        }
