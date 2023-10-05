from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from news.models import Post

from .models import UpcomingEventsPlugin, Event, CalendarEventsPlugin

@plugin_pool.register_plugin
class UpcomingEventsPluginPublisher(CMSPluginBase):
    model = UpcomingEventsPlugin
    render_template = 'events/plugins/upcoming_events.html'
    name = "Ближайшие мероприятия"
    module = "Мероприятия"

    def render(self, context, instance, placeholder):
        context.update({
            'id': instance.generate_id(),
        })
        context['object_list'] = instance.get_objects()
        return context


@plugin_pool.register_plugin
class CalendarEventsPluginPublisher(CMSPluginBase):
    model = CalendarEventsPlugin
    render_template = 'events/plugins/calendar.html'
    name = "Календарь мероприятий"
    module = "Мероприятия"

    def render(self, context, instance, placeholder):
        context.update({
            'id': instance.generate_id(),
        })
        context['object_list'] = instance.get_objects()
        events_dates_qs = Event.objects.upcoming() \
                            .values_list('start_at__date') \
                            .distinct() \
                            .order_by()
        
        context['events_dates'] = [date[0].strftime("%Y-%m-%d") for date in events_dates_qs]
        return context
