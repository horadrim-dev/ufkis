from django.contrib import admin

from django.db.utils import ProgrammingError
from .models import Category, Catalog



# class CategoryInline(admin.TabularInline):
#     model = Category
#     exclude = []
#     extra = 0
#     # formset = ModuleContentInlineFormSet
#     # raw_id_fields = ("content_post", )
#     # class Media:
#     #     js = ('grid/js/modulecontent_inline.js',)

# class CatalogAdmin(admin.ModelAdmin):
#     pass
#     # inlines = (CategoryInline, )

 
# admin.site.register(Catalog, CatalogAdmin)