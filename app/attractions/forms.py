from django import forms
from .models import Attraction, Category

class AttractionForm(forms.ModelForm):
    class Meta:
        model = Attraction
        # fields = []
        exclude = []

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = []
        exclude = []

class FilterForm(forms.Form):
    template_name = 'attractions/includes/filter_form.html'

    category = forms.ModelChoiceField(
        label='Категория',
        required=False,
        queryset=Category.objects,
        widget=forms.CheckboxSelectMultiple()
    )