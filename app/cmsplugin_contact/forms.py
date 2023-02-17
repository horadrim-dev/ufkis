from django import forms
from django.utils.translation import ugettext_lazy as _
#import settings
from cmsplugin_contact.nospam.forms import BaseForm, HoneyPotForm, RecaptchaForm, AkismetForm
  
class ContactForm(forms.Form):
    email = forms.EmailField(label=_("Email"), widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ваш email адрес'}))
    subject = forms.CharField(label=_("Subject"), required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Тема сообщения'}))
    content = forms.CharField(label=_("Content"), 
                            widget=forms.Textarea(attrs={
                                                         'class':'form-control', 
                                                         'placeholder':'Сообщение',
                                                         'rows':'5'
                            }))
    pd_agreement = forms.BooleanField(label="Даю согласие на обработку персональных данных", 
                            widget=forms.CheckboxInput()
                            )

    template = "cmsplugin_contact/contact.html"
  
class HoneyPotContactForm(HoneyPotForm):
    pass

class AkismetContactForm(AkismetForm):
    akismet_fields = {
        'comment_author_email': 'email',
        'comment_content': 'content'
    }
    akismet_api_key = None
    

# class RecaptchaContactForm(RecaptchaForm):
class RecaptchaContactForm(BaseForm):
    pass
#     recaptcha_public_key = None
#     recaptcha_private_key = None
#     recaptcha_theme = None
