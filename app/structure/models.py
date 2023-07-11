from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from core.models import OrderedModel



class StructureBase(OrderedModel):

    # def save(self, lock_recursion=False, *args, **kwargs):

    #     super().save(*args, **kwargs)

    #     if not lock_recursion:
    #         self.update_order(
    #             list_of_objects = list(
    #                 Attraction.objects.filter(category=self.category, season=self.season).exclude(id=self.id)
    #                 )
    #         )
    
    class Meta:
        abstract = True



class Organization(StructureBase):
    parent = models.ForeignKey('Organization', verbose_name="Родительская организация",
                            on_delete=models.SET_NULL,
                            blank=True, null=True,)
    name = models.CharField(verbose_name="Полное название", max_length=256)
    short_name = models.CharField(verbose_name="Краткое название", max_length=128, 
                                  blank=True, null=True)
    address = models.CharField(verbose_name="Адрес", max_length=256)
    site = models.URLField(verbose_name="Сайт", blank=True, null=True)
    description = HTMLField(verbose_name="Описание", blank=True, null=True)
    logo = FilerImageField(verbose_name="Логотип", 
                           on_delete=models.CASCADE, 
                           blank=True, null=True)

    # PRIEM
    # DOCUMENT (основной документ, положение, устав)
    # ВИДЫ ДЕЯТЕЛЬНОСТИ? (САМБО ДЗЮДО И т.д.)
    class Meta:
        verbose_name = "организация"
        verbose_name_plural = "организации"

    def __str__(self):
        return self.name
    
    def get_otdels(self):
        return self.otdel_set.all()

class Otdel(StructureBase):
    organization = models.ForeignKey(Organization, verbose_name="Организация",
                                     on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=256)
    # PHONEs

    class Meta:
        verbose_name = "отдел"
        verbose_name_plural = "отделы"

    def __str__(self):
        return "[{}] {}".format(self.organization.short_name, self.name)


class Sotrudnik(StructureBase):
    organization = models.ForeignKey(Organization, verbose_name="Организация",
                                     on_delete=models.CASCADE)
    otdel = models.ForeignKey(Otdel, verbose_name="Отдел",
                            on_delete=models.SET_NULL,
                            blank=True, null=True,
                            help_text="Если не заполнено, сотрудник будет \
                                отображаться в разделе \"Прочие сотрудники\" организации")
    lastname = models.CharField(verbose_name="Фамилия", max_length=32)
    firstname = models.CharField(verbose_name="Имя", max_length=32)
    surname = models.CharField(verbose_name="Отчество", max_length=32)
    position = models.CharField(verbose_name="Должность", max_length=128)
    photo = FilerImageField(verbose_name="Фото", 
                           on_delete=models.CASCADE, 
                           blank=True, null=True)
    in_apparat = models.BooleanField(verbose_name="В аппарате управления",
                                  default=False,
                                  help_text="Если отмечено, сотрудник будет выведен \
                                  в разделе \"Аппарат управления\" организации")
    # PHONE

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"

    def __str__(self):
        return " ".join([str(self.lastname), str(self.firstname), str(self.surname)])
