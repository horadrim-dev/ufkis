from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

# from .models import DocumentsPlugin, DocumentPlugin

# @plugin_pool.register_plugin
# class DocumentsPlugin(CMSPluginBase):
#     """Выводит документы определенной категории"""

#     model =  DocumentsPlugin
#     render_template = 'docs/documents.plugin.html'
#     name = "Документы"   
#     module = "Документы"

#     def render(self, context, instance, placeholder):

#         context.update({
#             'id': instance.generate_id(),
#             'instance': instance,
#             'object_list': instance.related_documents(),
#             'SHOW_DESCRIPTION': instance.show_description,
#             'SHOW_ICON': instance.show_icon,
#             # 'SHOW_LINK': instance.show_link,
#             'SHOW_FILE_ATTRS': instance.show_file_attrs,
#             'SHOW_TAGS': instance.show_tags,
#             'BOOTSTRAP_COL': instance.bootstrap_col
#         })

#         return context