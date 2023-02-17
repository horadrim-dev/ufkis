from logging import Filter
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Attraction
from .forms import FilterForm
from django.contrib import messages
from django_filters.views import FilterView
from .filtersets import AttractionFilterSet

class AttractionListView( FilterView):
    template_name = 'attractions/attraction_list.html'
    # model = Attraction
    filterset_class = AttractionFilterSet
    # filter_form = FilterForm
    # filter_data = None

    # def setup(self, request, *args, **kwargs):
    #     super().setup(request, *args, **kwargs)

    #     # валидируем get параметры формы - фильтра
    #     form = FilterForm(request.GET)
    #     if not form.is_valid():
    #         messages.warning(
    #             request,
    #             'Некорректные параметры запроса: ["{}"]'
    #             .format(', '.join(form.errors.keys()))
    #         )
    #     self.filter_data = form.cleaned_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # assert False, dir(context['filter'])
        # context['filter_form'] = self.filter_form
        return context


class AttractionDetailView(DetailView):
    template_name = 'attractions/attraction_detail.html'
    model = Attraction

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['added_breadcrumbs'] = [{'url':self.object.get_absolute_url, 'title':self.object.title}]
        context['page_title'] = self.object.title
        return context