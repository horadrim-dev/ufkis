from django.views.generic import ListView, DetailView, View, TemplateView
from django.db.models.functions import TruncDay
from .models import Event

class EventsListView(ListView):
    template_name = "events/event_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.upcoming().annotate(day=TruncDay('start_at'))
    