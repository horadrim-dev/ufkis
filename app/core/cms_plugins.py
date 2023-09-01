from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import HeaderPlugin, WhitespacePlugin

@plugin_pool.register_plugin
class HeaderPluginPublisher(CMSPluginBase):
    module = "Общий"
    name = "Заголовок"
    model = HeaderPlugin
    allow_children = False
    render_template = "core/plugins/header.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['title'] = instance.title
        context['subtitle'] = instance.subtitle
        context['layout'] = instance.layout
        context['align'] = instance.align
        return context

@plugin_pool.register_plugin
class WhitespacePluginPublisher(CMSPluginBase):
    module = "Общий"
    name = "Пустое место"
    model = WhitespacePlugin
    allow_children = False
    render_template = "core/plugins/whitespace.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['size'] = instance.size
        return context