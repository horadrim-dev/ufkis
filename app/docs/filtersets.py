import django_filters
from django import forms
from .models import Document, Category, DocumentType
from taggit.models import Tag
from taggit.managers import TaggableManager
from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget

# class TagFilter(django_filters.CharFilter):
#     field_class = TagField

#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault('lookup_expr', 'in')
#         super().__init__(*args, **kwargs)

    

class DocumentFilterSet(django_filters.FilterSet):

    category = django_filters.filters.ModelChoiceFilter(
        queryset=Category.objects.all(), 
        blank=True,
        empty_label='Все документы',
        widget=forms.RadioSelect(attrs={'class':'hidden autoapply'})
        )
    number = django_filters.filters.NumberFilter(
        widget= forms.DateInput(attrs={'class': 'form-control'}),
    )
    date = django_filters.filters.DateFilter(
        widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    name = django_filters.CharFilter(lookup_expr='icontains',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
    )
    # document_type = django_filters.filters.ModelChoiceFilter(
    #     queryset=DocumentType.objects.all(), 
    #     blank=True,
    #     empty_label='Все типы документов',
    #     widget=forms.RadioSelect(attrs={'class':'hidden autoapply'})
    #     )
    # tags = TagFilter(
    #     field_name='tags__name',
    #     widget=LabelWidget(attrs={'class':'tags'})
    #     )
    # start_date = django_filters.filters.DateFilter(field_name='date',
    #     widget= forms.DateInput(attrs={'class': 'form-control autoapply', 'type': 'date'}),
    #     lookup_expr='gte', label='от')
    # end_date = django_filters.filters.DateFilter(field_name='date',
    #     widget= forms.DateInput(attrs={'class': 'form-control autoapply', 'type': 'date'}),
    #     lookup_expr='lte', label='до')
    # tags = django_filters.filters.ModelMultipleChoiceField(
    #     blank=True,
    #     # empty_label='Все новости',
    #     name='tags__name',
    #     to_field_name='name',
    #     conjoined=True,
    #     distinct=True,
    #     queryset=Tag.objects.all(), 
    #     widget=forms.CheckboxSelectMultiple(attrs={'class':''})
    #     )
    # season = django_filters.filters.ChoiceFilter(
    #     choices=SEASON_CHOICES, 
    #     empty_label='<i class="bi bi-funnel"></i>',
    #     widget=forms.RadioSelect(attrs={'class':'btn-check'})
    #     )

    # def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
    #     super().__init__(data, queryset, request=request, prefix=prefix)
    #     self.form.initial['work_in_summer'] =True

    class Meta:
        model = Document
        # fields = ['category', 'tags']
        # исключаем автоматическую генерацию фильтров для этих полей, заданы вручную в теле класса
        exclude = ['category', 'tags', 'date', 'name']
        
        # filter_overrides = {
        #     TaggableManager: {
        #         'filter_class': django_filters.ModelChoiceFilter, 
        #         # 'extra': lambda f: {
        #         #     'queryset': remote_model(f)._default_manager.complex_filter(
        #         #         remote_field(f).limit_choices_to),
        #         # }
        #     },
        # }