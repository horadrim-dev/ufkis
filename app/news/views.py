from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post
from django_filters.views import FilterView
from .filtersets import PostFilterSet

class PublishedObjectsMixin:

    def get_queryset(self):
        if self.request.toolbar and self.request.toolbar.edit_mode_active:
            return Post.objects.all() # [:instance.num_objects]
        else:
            return Post.objects.published() # [:instance.num_objects]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["css_styles"] = [str(context)]
    #     return context
    

class PostListView(PublishedObjectsMixin, FilterView):
    template_name = 'news/post_list.html'
    # model = Post
    paginate_by = 12
    filterset_class = PostFilterSet

# class PostListView(ListView):
#     template_name = 'news/post_list.html'
#     model = Post
#     paginate_by = 12

    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
    #     assert False, (context['filter'].form['tags'], dir(context['filter'].form['tags']))

class PostDetailView(PublishedObjectsMixin, DetailView):
    template_name = 'news/post_detail.html'
    slug_field = 'alias'
    model = Post

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['added_breadcrumbs'] = [{'url':self.object.get_absolute_url, 'title':self.object.title}]
        context['page_title'] = self.object.title
        return context