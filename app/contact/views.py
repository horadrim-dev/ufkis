from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, FileResponse
from django.views.generic import ListView, DetailView, View, TemplateView
from django.core.exceptions import PermissionDenied
from django_filters.views import FilterView
from cms.models.pluginmodel import CMSPlugin
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse
import os

class ContactTemplateView(TemplateView):
    template_name = "contact/base.html"

# class DocumentDetailView(DetailView):
#     template_name = 'docs/document_detail.html'
#     slug_field = 'id'
#     model = Document

#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         context['added_breadcrumbs'] = [{'url':self.object.get_absolute_url, 'title':self.object.name}]
#         context['page_title'] = self.object.name
#         return context
    
