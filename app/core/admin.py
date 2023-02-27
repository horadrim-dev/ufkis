from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import IconExtension

from django.db.utils import ProgrammingError
from .models import SiteSettings, Social


class IconExtensionAdmin(PageExtensionAdmin):
    pass

class SocialInline(admin.StackedInline):
    model = Social
    exclude = []
    extra = 0
    # formset = ModuleContentInlineFormSet
    # raw_id_fields = ("content_post", )
    # class Media:
    #     js = ('grid/js/modulecontent_inline.js',)

class SiteSettingsAdmin(admin.ModelAdmin):

    inlines = (SocialInline, )

    # Create a default object on the first page of SiteSettingsAdmin with a list of settings
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        # be sure to wrap the loading and saving SiteSettings in a try catch,
        # so that you can create database migrations
        try:
            SiteSettings.load().save()
        except ProgrammingError:
            pass
 
    # prohibit adding new settings
    def has_add_permission(self, request, obj=None):
        return False
 
    # as well as deleting existing
    def has_delete_permission(self, request, obj=None):
        return False
 
 
admin.site.register(IconExtension, IconExtensionAdmin)
admin.site.register(SiteSettings, SiteSettingsAdmin)