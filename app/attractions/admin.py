from django.contrib import admin
from .models import *
from .forms import AttractionForm, CategoryForm
from cms.admin.placeholderadmin import PlaceholderAdminMixin

class PhotoAttractionInline(admin.TabularInline):
    model = Photo

@admin.register(Attraction)
class AttractionsAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    # поле alias будет автоматически заполнено на основе заголовка
    # prepopulated_fields = {
    #     "alias" : ("title",)
    # 
    list_filter = ('category', 'season',)
    list_display = ['title', 'category', 'season', 'order']
    form = AttractionForm
    inlines = (PhotoAttractionInline, )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm