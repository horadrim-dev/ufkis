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
        })
        return context

