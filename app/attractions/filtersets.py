from unicodedata import category
import django_filters
from django import forms
from .models import Attraction, Category, SEASON_CHOICES


class AttractionFilterSet(django_filters.FilterSet):

    category = django_filters.filters.ModelChoiceFilter(
        queryset=Category.objects, 
        blank=True,
        empty_label='<i class="bi bi-funnel"></i>',
        widget=forms.RadioSelect(attrs={'class':'btn-check'})
        )
    season = django_filters.filters.ChoiceFilter(
        choices=SEASON_CHOICES, 
        empty_label='<i class="bi bi-funnel"></i>',
        widget=forms.RadioSelect(attrs={'class':'btn-check'})
        )

    # def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
    #     super().__init__(data, queryset, request=request, prefix=prefix)
    #     self.form.initial['work_in_summer'] =True

    class Meta:
        model = Attraction
        fields = ['category', 'season']