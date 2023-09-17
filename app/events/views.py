from django.views.generic import ListView, DetailView, View, TemplateView

class EventsListView(TemplateView):
    template_name = "events/event_list.html"