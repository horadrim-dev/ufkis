from django.db import models
from core.models import SingletonModel
from djangocms_text_ckeditor.fields import HTMLField

# Create your models here.

class ContactSettings(SingletonModel):
    # site_url = models.URLField(verbose_name=_('Website url'), max_length=256)
    agreement_title = models.CharField("Название этапа ознакомления с соглашением", max_length=256,
        default="Прочитайте правила пользования виртуальной приемной")
    agreement = HTMLField("Соглашение", configuration='CKEDITOR_SETTINGS_POST', default="")
    agreement_checkbox_text = models.CharField("Текст галочки на форме соглашения", max_length=256,
        default="Я прочитал(а) правила пользования виртуальной приемной")
    userdata_title = models.CharField("Название этапа ввода пользовательских данных", max_length=256,
        default="Укажите данные о себе")
    target_email = models.EmailField(verbose_name='E-mail', blank=True, null=True,
                                     help_text="На этот адрес будут приходить обращения из виртуальной приемной")
    userdata_form_text = HTMLField("Текст на форме данных пользователя", configuration='CKEDITOR_SETTINGS_POST', default="")
    userdata_checkbox_text = models.CharField("Текст галочки на форме данных пользователя", max_length=256,
        default="Я соглашаюсь на обработку моих персональны данных")
    message_title = models.CharField("Название этапа заполнения обращение", max_length=256,
        default="Заполните и отправьте обращение")
    message_form_text = HTMLField("Текст на форме заполнения обращения ", configuration='CKEDITOR_SETTINGS_POST', default="")

    success_text = HTMLField("Текст после успешной отправки обращения ", default="")

    valid_file_extensions = models.CharField("Разрешенные форматы файлов (через запятую)", max_length=512,
                                             default="pdf, txt, doc, docx, xls, xlsx, ppt, pptx, odt, ods, odp, jpg, png, gif, tiff, zip")


    def __str__(self):
        return 'Конфигурация виртуальной приемной'

    class Meta:
        verbose_name = "Конфигурация"
        verbose_name_plural = "Конфигурация"

    