from ast import Num
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from .models import AnimatedNumbers, Number

class NumberInline(admin.TabularInline):
    model = Number
    extra = 0

@plugin_pool.register_plugin
class AnimatedNumbersPlugin(CMSPluginBase):
    model = AnimatedNumbers
    name = "Блок с анимированными показателями"
    render_template = "animated_numbers.html"
    cache = True
    inlines = (NumberInline, )

    def render(self, context, instance, placeholder):
        context.update({
            'id': instance.generate_id(),
            'duration': instance.duration,
            'numbers': instance.get_numbers(),
        })
        return context

