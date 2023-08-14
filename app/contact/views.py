from typing import Any
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, FileResponse
from django.views.generic import ListView, DetailView, View, TemplateView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from formtools.wizard.views import CookieWizardView
from .forms import AgreementForm, UserDataForm, MessageForm
from .models import ContactSettings

class ContactWizard(CookieWizardView):

    form_list = [AgreementForm, UserDataForm, MessageForm]
    template_name = 'contact/form.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # загружаем модель с настройками приложения
        self.settings = ContactSettings.load()
        

    def done(self, form_list, **kwargs):
        return render(self.request, 'contact/success.html', {
            'form_data': [form.cleaned_data for form in form_list],
            'SUCCESS_TEXT': self.settings.success_text,
        })
