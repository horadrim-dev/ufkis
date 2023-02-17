from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from .models import Reviews, Review


@plugin_pool.register_plugin
class ReviewsPlugin(CMSPluginBase):
    model = Reviews
    name = "Отзывы"
    render_template = "reviews.html"
    cache = True

    def render(self, context, instance, placeholder):
        context.update({
            'id': instance.generate_id(),
            'reviews': instance.get_reviews(),
        })
        return context

