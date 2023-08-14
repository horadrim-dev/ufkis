from django.contrib import admin
from core.admin import SingletonModelAdmin
from .models import ContactSettings
# Register your models here.

@admin.register(ContactSettings)
class ContactSettingsAdmin(SingletonModelAdmin):
    model = ContactSettings