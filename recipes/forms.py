from django.forms import ModelForm, ModelChoiceField
from django import forms
from mptt.forms import TreeNodeChoiceField, TreeNodeMultipleChoiceField
from .models import RecipeCategory, Embed
from dal import autocomplete

class SubmitEmbed(forms.Form):
    url = forms.URLField(label='Adres przepisu')

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
