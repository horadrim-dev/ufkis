from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from core.models import OrderedModel



class StructureBase(OrderedModel):

    
    class Meta:
        abstract = True



class Organization(StructureBase):
    parent = models.ForeignKey('self', verbose_name="Родительская организация",
                            on_delete=models.SET_NULL,
                            blank=True, null=True,)
    # уровень вложенности записи
    level = models.PositiveSmallIntegerField(default=1, blank=True, null=True)
    # номер в общем списке, учитывая древовидную структуру
    list_order = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    name = models.CharField(verbose_name="Полное название", max_length=256)
    short_name = models.CharField(verbose_name="Краткое название", max_length=128, )
    address = models.CharField(verbose_name="Адрес", max_length=256)
    site = models.URLField(verbose_name="Сайт", blank=True, null=True)
    description = HTMLField(verbose_name="Описание", blank=True, null=True)
    logo = FilerImageField(verbose_name="Логотип", 
                           on_delete=models.CASCADE, 
                           blank=True, null=True)

    # PRIEM?
    # DOCUMENT (основной документ, положение, устав)?
    # ВИДЫ ДЕЯТЕЛЬНОСТИ? (САМБО ДЗЮДО И т.д.)?

    def __str__(self):
        return self.short_name
    
    def leveled_name(self):
        if self.level > 1:
            return '|---' * (self.level - 1) + self.name
        else:
            return self.name

    leveled_name.short_description = "Название"

    
    def get_otdels(self):
        return self.otdel_set.all()
    
    def update_list_order(self, parent_id=None, start_order=1):
        '''обновляет порядок всех элементов при выводе списком'''
        # получаем соседние объекты
        menus = list(Organization.objects.filter(parent_id=parent_id).order_by('order'))
        if len(menus) == 0:
            return start_order

        new_order = start_order
        for obj in menus:
            obj.list_order = new_order
            obj.save(update_fields=['list_order'], lock_recursion=True)
            new_order = obj.update_list_order(parent_id=obj.id, start_order= new_order + 1)
        return new_order

    def save(self, lock_recursion=False, *args, **kwargs):
        if self.parent_id:
            self.level = Organization.objects.get(id=self.parent_id).level + 1
        else:
            self.level = 1

        super().save(*args, **kwargs)

        # save method для OrderedModel
        if not lock_recursion:
            self.update_order(
                list_of_objects = list(
                    Organization.objects.filter(parent=self.parent).exclude(id=self.id)
                    )
            )
            # обновляем номера в общем списке
            self.update_list_order()

    class Meta:
        ordering = ['list_order' ]
        verbose_name = "организация"
        verbose_name_plural = "организации"


class Otdel(StructureBase):
    organization = models.ForeignKey(Organization, verbose_name="Организация",
                                     on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=256)
    # PHONEs?


    def __str__(self):
        return self.name

    def save(self, lock_recursion=False, *args, **kwargs):
        # save method для OrderedModel
        super().save(*args, **kwargs)

        if not lock_recursion:
            self.update_order(
                list_of_objects = list(
                    Otdel.objects.filter(organization=self.organization).exclude(id=self.id)
                    )
            )

    class Meta:
        ordering = ['organization', 'order' ]
        verbose_name = "отдел"
        verbose_name_plural = "отделы"


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
    # PHONE?


    def name(self):
        return "{} {} {}".format(self.lastname, self.firstname, self. surname)
    name.short_description = "ФИО"

    def __str__(self):
        return " ".join([str(self.lastname), str(self.firstname), str(self.surname)])

    def save(self, lock_recursion=False, *args, **kwargs):
        # save method для OrderedModel
        super().save(*args, **kwargs)

        if not lock_recursion:
            self.update_order(
                list_of_objects = list(
                    Sotrudnik.objects.filter(organization=self.organization, otdel=self.otdel).exclude(id=self.id)
                    )
            )

    class Meta:
        ordering = ['organization', 'otdel', 'order' ]
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"