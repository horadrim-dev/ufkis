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
from filer.fields.file import FilerFileField
from django.core.validators import FileExtensionValidator
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


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
    lastname = forms.CharField(label="Фамилия",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Укажите вашу фамилию"
        })
    )
    firstname = forms.CharField(label="Имя",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Укажите ваше имя"
        })
    )
    middlename = forms.CharField(label="Отчество",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Укажите ваше отчество"
        })
    )
    email = forms.EmailField(label="Электронная почта",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Укажите ваш адрес электронной почты"
        })
    )
    phone = PhoneNumberField(label="Телефон")

    agree = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            "class": "form-control form-value checkbox",
            "placeholder": "+7 1112223344"
        })
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.html_before_form = self.settings.userdata_form_text
        self.fields['agree'].label = self.settings.userdata_checkbox_text

class MessageForm(ContactForm):
    subject = forms.CharField(
        label="Тема обращения",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Укажите суть обращения"
        })
    )
    message = forms.CharField(
        label="Текст обращения",
        widget=forms.Textarea(attrs={
            "class": "form-control",
        })
    )
    attachment_1 = forms.FileField(required=False, 
                                   widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    attachment_2 = forms.FileField(required=False, 
                                   widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    attachment_3 = forms.FileField(required=False, 
                                   widget=forms.ClearableFileInput(attrs={"class": "form-control"}))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.html_before_form = self.settings.message_form_text
        # загружаем разрешенные расширения файлов из настроек в валидатор
        validators_list = [FileExtensionValidator(self.settings.valid_extensions)]
        self.fields['attachment_1'].validators = validators_list
        self.fields['attachment_2'].validators = validators_list
        self.fields['attachment_3'].validators = validators_list

        
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