from django.contrib import admin
from .models import Event, CategoryEvent
# Register your models here.

@admin.register(CategoryEvent)
class CategoryEventAdmin(admin.ModelAdmin):
    model = CategoryEvent

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('name', 'category', 'start_at')

