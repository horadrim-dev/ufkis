from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import ColumnsForm
from .models import Column, Columns

@plugin_pool.register_plugin
class ColumnsPlugin(CMSPluginBase):
    model = Columns
    module = _("Columns")
    name = _("Columns")
    render_template = "djangocms_columns/columns.html"
    allow_children = True
    child_classes = ["ColumnPlugin"]
    form = ColumnsForm

    def save_model(self, request, obj, form, change):
        response = super().save_model(
            request, obj, form, change
        )
        for _x in range(int(form.cleaned_data['create'])):
            col = Column(
                parent=obj,
                placeholder=obj.placeholder,
                language=obj.language,
                # width=form.cleaned_data['create_width'],
                classes="",
                position=CMSPlugin.objects.filter(parent=obj).count(),
                plugin_type=ColumnPlugin.__name__
            )
            col.save()
        return response


@plugin_pool.register_plugin
class ColumnPlugin(CMSPluginBase):
    model = Column
    module = _("Columns")
    name = _("Column")
    render_template = "djangocms_columns/column.html"
    parent_classes = ["ColumnsPlugin"]
    allow_children = True


