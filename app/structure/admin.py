from django.contrib import admin
from .models import *
from .forms import *
from cms.admin.placeholderadmin import PlaceholderAdminMixin

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    form = OrganizationForm
    list_display = ('leveled_name', 'order', )
    exclude = ['level', 'list_order']

@admin.register(Otdel)
class OtdelAdmin(admin.ModelAdmin):
    form = OtdelForm
    list_display = ('name', 'organization', 'order', )
    list_filter = ["organization" ]


@admin.register(Sotrudnik)
class SotrudnikAdmin(admin.ModelAdmin):
    form = SotrudnikForm
    list_display = ('name', 'organization', 'otdel', 'order', )
    list_filter = ["organization", "otdel"]