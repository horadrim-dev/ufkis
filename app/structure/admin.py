from django.contrib import admin
from .models import *
from .forms import *
from cms.admin.placeholderadmin import PlaceholderAdminMixin

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    # поле alias будет автоматически заполнено на основе заголовка
    # prepopulated_fields = {
    #     "alias" : ("title",)
    # 
    form = OrganizationForm
    # exclude = ['published']

@admin.register(Otdel)
class OtdelAdmin(admin.ModelAdmin):
    form = OtdelForm


@admin.register(Sotrudnik)
class SotrudnikAdmin(admin.ModelAdmin):
    form = SotrudnikForm