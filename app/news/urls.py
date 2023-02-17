from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
] 

