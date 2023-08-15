from typing import Any, List
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

FORM_TEMPLATES = {0: 'contact/form_agreement.html',
                  1: 'contact/form_userdata.html',
                  2: 'contact/form_message.html'}
class ContactWizard(CookieWizardView):

    form_list = [AgreementForm, UserDataForm, MessageForm]
    # template_name = 'contact/form.html'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # загружаем модель с настройками приложения
        self.settings = ContactSettings.load()

    def get_template_names(self):
        return [FORM_TEMPLATES[int(self.steps.current)]]

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form, **kwargs)
        context.update({
            'STEP_1': self.settings.agreement_title,
            'STEP_2': self.settings.userdata_title,
            'STEP_3': self.settings.message_title,
        })
        return context 

    def done(self, form_list, **kwargs):
        return render(self.request, 'contact/success.html', {
            'form_data': [form.cleaned_data for form in form_list],
            'SUCCESS_TEXT': self.settings.success_text,
        })
