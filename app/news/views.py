from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import PermissionDenied
from .models import Post
from django_filters.views import FilterView
from .filtersets import PostFilterSet
from cms.models.pluginmodel import CMSPlugin
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

class PublishedObjectsMixin:

    def get_queryset(self):
        if self.request.toolbar: # and self.request.toolbar.edit_mode_active:
            return Post.objects.all() # [:instance.num_objects]
        else:
            return Post.objects.published() # [:instance.num_objects]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ADMIN_MODE"] = self.request.user.is_authenticated
        context["EDIT_MODE"] = True if self.request.toolbar.edit_mode_active else False
        return context
    

class PostListView(PublishedObjectsMixin, FilterView):
    template_name = 'news/post_list.html'
    # model = Post
    paginate_by = 12
    filterset_class = PostFilterSet


class PostDetailView(PublishedObjectsMixin, DetailView):
    template_name = 'news/post_detail.html'
    slug_field = 'alias'
    model = Post

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['added_breadcrumbs'] = [{'url':self.object.get_absolute_url, 'title':self.object.title}]
        context['page_title'] = self.object.title
        return context
    


ACTION_LIST = ("toggle-publish-state", )
RESULTS = {
    0 : "error",
    1 : "success",
}

class AdminView(View):


    def dispatch(self, request, *args, **kwargs):

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return self.ajax_post(request, *args, **kwargs)

        return super().dispatch(request, *args, **kwargs)
    

    def ajax_post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            raise PermissionDenied

        action = request.POST.get("action")
        post = request.POST.get("post")

        if action not in ACTION_LIST:
            raise Http404

        try:
            post = Post.objects.get(pk=post)
        except Post.DoesNotExist:
            raise Http404
        
        if post and (action == 'toggle-publish-state'):
            try:
                return self.toggle_publish_state_post(request, post)
            except PermissionDenied:
                return JsonResponse({"result": RESULTS[0], "message": "Нет прав доступа для этой операции"})

        raise Http404
    

    @method_decorator(permission_required("news.change_post", raise_exception=True))
    def toggle_publish_state_post(self, request, post:Post):
        '''Switching publish state of Post'''
        if post.published:
            post.published = False
            post.save()
            return JsonResponse({"result": RESULTS[1], "message": "Снято с публикации"})
        else:
            # if post has child plugins
            if CMSPlugin.objects.filter(placeholder_id=post.content_id).count() > 0:
                post.published = True
                post.save()
                return JsonResponse({"result": RESULTS[1], "message": "Опубликовано"})
            else: # no child plugins
                message = "Новость пуста и поэтому не может быть опубликована. \n Добавьте плагинов на страницу."
                return JsonResponse({"result": RESULTS[0], "message": message})
