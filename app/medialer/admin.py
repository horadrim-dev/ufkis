from django.contrib import admin
from .models import *
from .forms import *
from cms.admin.placeholderadmin import PlaceholderAdminMixin

@admin.register(AlbumPicture)
class AlbumPictureAdmin(admin.ModelAdmin):
    # поле alias будет автоматически заполнено на основе заголовка
    # prepopulated_fields = {
    #     "alias" : ("title",)
    # 
    form = AlbumPictureForm
    exclude = []

# @admin.register(Category)
# class PostAdmin( PlaceholderAdminMixin, admin.ModelAdmin):
#     form = CategoryForm