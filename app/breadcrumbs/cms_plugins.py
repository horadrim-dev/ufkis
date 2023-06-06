from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Breadcrumbs

@plugin_pool.register_plugin
class BreadcrumbsPlugin(CMSPluginBase):
    model = Breadcrumbs
    render_template = 'breadcrumbs/base.html'
    name = "Breadcrumbs"
    allow_children = False


    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'block_height': instance.height,
            'image': instance.image,
            'width_height_thumb': instance.width_height_thumb
        })
        if instance.title:
            context['page_title'] = instance.title
        return context

