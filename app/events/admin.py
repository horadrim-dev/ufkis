from django.contrib import admin
from .models import Event, CategoryEvent, DayEvent
from .forms import DayEventStackedInlineFormSet

@admin.register(CategoryEvent)
class CategoryEventAdmin(admin.ModelAdmin):
    model = CategoryEvent


class DayEventStackedInline(admin.StackedInline):
    model = DayEvent
    extra = 0
    # exclude = ['postfix_name']
    formset = DayEventStackedInlineFormSet

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('name', 'category',)
    inlines = (DayEventStackedInline, )