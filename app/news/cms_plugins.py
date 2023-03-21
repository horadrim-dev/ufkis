from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from .models import NewsPlugin

@plugin_pool.register_plugin
class NewsPlugin(CMSPluginBase):
    model =  NewsPlugin
    render_template = 'news/news_plugin.html'
    name = "Новости"   

    def render(self, context, instance, placeholder):
        context.update({
            'id': instance.generate_id(),
            'instance': instance,
            'object_list' : instance.get_objects(limit=instance.num_objects),
        })
        return context

