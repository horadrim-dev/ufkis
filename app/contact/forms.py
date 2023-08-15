from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *
from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget
from django.urls import reverse_lazy
from phonenumber_field.formfields import PhoneNumberField
from .models import ContactSettings

class ContactForm(forms.Form):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # загружаем модель с настройками приложения
        self.settings = ContactSettings.load()

class AgreementForm(ContactForm):
    agree = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            "class": "form-control form-value checkbox"
        })
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.html_before_form = self.settings.agreement
        self.fields['agree'].label = self.settings.agreement_checkbox_text

class UserDataForm(ContactForm):
    sender = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control"
        })
    )
    agree = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            "class": "form-control"
        })
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.html_before_form = self.settings.userdata_form_text
        self.fields['agree'].label = self.settings.userdata_checkbox_text

class MessageForm(ContactForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control"
        })
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.html_before_form = self.settings.message_form_text

# class DocumentForm(forms.ModelForm):

#     tags = TagField(required=False, widget=LabelWidget)

#     class Meta:
#         model = Document
#         # fields = []
#         exclude = ["extension"]

#     def clean(self):
#         cleaned_data = super().clean()
#         doc_file = cleaned_data.get("document_file")
#         doc_url = cleaned_data.get("document_url")

#         # try:
#         #     post = Post.objects.get(alias=slug)
#         # except Post.DoesNotExist:
#         #     post = None

#         if doc_file and doc_url:
#             msg = "Поля \"Файл документа\" и \"Ссылка на документ\" не должны быть заполнены одновременно."
#             self.add_error("document_url", msg)
#         if not doc_file and not doc_url:
#             msg = "Загрузите файл документа или введите ссылку на него."
#             self.add_error("document_file", msg)