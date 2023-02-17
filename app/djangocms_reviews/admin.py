from django.contrib import admin
from .models import Review
from .forms import ReviewForm


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # поле alias будет автоматически заполнено на основе заголовка
    # prepopulated_fields = {
    #     "alias" : ("title",)
    # 
    form = ReviewForm