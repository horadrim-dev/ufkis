from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from news.models import Post

from .models import UpcomingEventsPlugin, Event

@plugin_pool.register_plugin
class UpcomingEventsPluginPublisher(CMSPluginBase):
    model = UpcomingEventsPlugin
    render_template = 'events/plugins/upcoming_events.html'
    name = "Ближайшие мероприятия"   
    module = "Мероприятия"

    def render(self, context, instance, placeholder):

        context.update({
            'id': instance.generate_id(),
            'instance': instance,
        })

        context['object_list'] = Event.objects.upcoming()[:instance.num_objects]

        return context


#
