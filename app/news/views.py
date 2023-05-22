from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import ListView, DetailView, View
from .models import Post
from django_filters.views import FilterView
from .filtersets import PostFilterSet
from cms.models.pluginmodel import CMSPlugin

class PublishedObjectsMixin:

    def get_queryset(self):
        if self.request.toolbar: # and self.request.toolbar.edit_mode_active:
            return Post.objects.all() # [:instance.num_objects]
        else:
            return Post.objects.published() # [:instance.num_objects]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ADMIN_MODE"] = True if self.request.toolbar else False
        context["EDIT_MODE"] = True if self.request.toolbar.edit_mode_active else False
        return context
    

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
    

# def publish_post(request):
#     return HttpResponse("<h1>YEA</h1><h1> ",str(), " </h1>")

ACTION_LIST = ("publish", "unpublish")
RESPONSES = {
    0 : "error",
    1 : "success",
}

class AdminView(View):

    def get(self, request):
        # return JsonResponse({"response":1, "message": "Опубликовано"})

        action = request.GET.get("action")
        post = request.GET.get("post")

        if action not in ACTION_LIST:
            raise Http404()

        try:
            p = Post.objects.get(pk=post)
        except Post.DoesNotExist:
            raise Http404()
        
        if post and (action == "publish"):
            # if post has child plugins
            if CMSPlugin.objects.filter(placeholder_id=p.content_id).count() > 0:
                p.published = True
                p.save()
                return JsonResponse({"response": RESPONSES[1], "message": "Опубликовано"})
            else: # no child plugins
                message = "Новость пуста и поэтому не может быть опубликована. \n Добавьте плагинов на страницу."
                return JsonResponse({"response": RESPONSES[0], "message": message})

        if post and (action == "unpublish"):
            p.published = False
            p.save()
            return JsonResponse({"response": RESPONSES[1], "message": "Снято с публикации"})
        raise Http404()