from django.contrib import admin
from .models import *
from .forms import PostForm
from cms.admin.placeholderadmin import PlaceholderAdminMixin

@admin.register(Post)
class PostAdmin( PlaceholderAdminMixin, admin.ModelAdmin):
    # поле alias будет автоматически заполнено на основе заголовка
    # prepopulated_fields = {
    #     "alias" : ("title",)
    # 
    form = PostForm
