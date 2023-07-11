from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # path('admin/', AdminView.as_view(), name='admin'),
    # path('ajax/otdels/<int:org_id>', GetOtdelsView.as_view(), name='get-otdels'),
    path('', OrganizationListView.as_view(), name='index'),
    # path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
] 

