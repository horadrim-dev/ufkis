from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', AttractionListView.as_view(), name='index'),
    path('<int:pk>/', AttractionDetailView.as_view(), name='detail'),
] 

