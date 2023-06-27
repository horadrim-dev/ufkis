from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import PermissionDenied
from django_filters.views import FilterView
from django.views.generic import TemplateView
from cms.models.pluginmodel import CMSPlugin
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from . import models

# NEWS_FILTER_STATES = ("visible", "hidden")

class MediaView(TemplateView):
    template_name = 'medialer/media.html'
    # model = Post
    # paginate_by = 12
    # filterset_class = MediaFilterSet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_pictures'] = models.PluginPicture.objects.all()[:8]
        context['albums'] = models.Album.objects.all()
        # context['news_filter_state'] = self.get_filter_state()
        # assert False, context
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)

        # # seting news list layout to cookie
        # response.set_cookie('news_list_layout', 
        #                     self.get_news_list_layout(),
        #                     path=reverse("news:index"),
        #                     max_age=3600*24*7)
        # # seting news filter state to cookie
        # response.set_cookie('news_filter_state', 
        #                     self.get_filter_state(),
        #                     path=reverse("news:index"),
        #                     max_age=3600*24*7)
        return response
    

class AlbumPictureListView(ListView):
    template_name = 'medialer/album.html'
    slug_field = 'album_id'
    # model = Album
