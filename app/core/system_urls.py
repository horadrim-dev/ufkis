from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('structure/', include("structure.system_urls")),
] 

