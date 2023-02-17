from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from .models import ColorBlocksModel, ColorBlock


class ColorBlockInlineAdmin(admin.StackedInline):
    model = ColorBlock
    extra = 0

@plugin_pool.register_plugin
class ColorBlocksPlugin(CMSPluginBase):
    model = ColorBlocksModel
    name = "Цветные блоки"
    render_template = "colorblocks.html"
    cache = True
    inlines = (ColorBlockInlineAdmin, )

    def render(self, context, instance, placeholder):
        context.update({
            'id': instance.generate_id(),
            'colorblocks': instance.get_colorblocks(),
        })
        return context

