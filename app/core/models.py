from django.db import models, transaction
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

class OrderedModel(models.Model):
    
    order = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name="Порядок", help_text="Если оставить равным 0 - добавится в конец.")

    def update_order(self, list_of_objects):
            '''обновляет порядок элементов с общим родителем'''
            # получаем соседние объекты
            objects = list_of_objects
            objects_count = len(objects)
            # формируем список новых ордеров
            orders = [i for i in range(1, objects_count + 1 + 1)]

            # если новый ордер за пределами возможных или равен 0
            if (self.order > objects_count + 1) or (self.order <= 0):

                with transaction.atomic():
                    # просто присваем последний ордер
                    self.order = orders[-1]
                    self.save(update_fields=['order'], lock_recursion=True)
                    # обновляем соседние меню
                    for i in orders[:-1]:
                        objects[i-1].order = i
                        objects[i-1].save(update_fields=['order'], lock_recursion=True)
                    
            else: # если новый ордер в пределах возможных
                # резервируем нужный ордер для изменяемого меню, другие меню расставляем по остальным ордерам
                obj_num = 0
                with transaction.atomic():
                    for i in orders:
                        if i != self.order:
                            objects[obj_num].order = i
                            objects[obj_num].save(update_fields=['order'], lock_recursion=True)
                            obj_num += 1

    class Meta:
        abstract = True
        ordering = ['order']



class IconExtension(PageExtension):
    ''' 
    Adding text font-awesome name icon to page 
    for displaying in menu 
    '''
    fa_icon = models.CharField(verbose_name="Иконка страницы",
                                help_text='Названия иконок брать <a href="https://fontawesome.com/v4/icons/" target="blank">отсюда</a>', 
                                max_length=32, default="", 
                                blank=True, )


extension_pool.register(IconExtension)


class SingletonModel(models.Model):
    """Singleton Django Model
    https://gist.github.com/senko/5028413

    Ensures there's always only one entry in the database, and can fix the
    table (by deleting extra entries) even if added via another mechanism.
    Also has a static load() method which always returns the object - from
    the database if possible, or a new empty (default) instance if the
    database is still empty. If your instance has sane defaults (recommended),
    you can use it immediately without worrying if it was saved to the
    database or not.
    Useful for things like system-wide user-editable settings.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Save object to the database. Removes all other entries if there
        are any.
        """
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        """
        Load object from the database. Failing that, create a new empty
        (default) instance of the object and return it (without saving it
        to the database).
        """

        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class SiteSettings(SingletonModel):
    # site_url = models.URLField(verbose_name=_('Website url'), max_length=256)
    title = models.CharField(verbose_name=_('Заголовок'), max_length=256, default="")
    subtitle = models.CharField(verbose_name=_('Подзаголовок'), max_length=256, default="")
    phone = models.CharField(verbose_name=_('Телефон'), max_length=256, default="")
    email = models.EmailField(verbose_name='E-mail', blank=True, null=True)
    address = models.CharField(verbose_name=_('Адрес'), max_length=256, default="")
    share_vk = models.BooleanField(verbose_name="Вконтакте", default=True)
    share_ok = models.BooleanField(verbose_name="Одноклассники", default=True)
    share_fb = models.BooleanField(verbose_name="Facebook", default=False)
    share_twitter = models.BooleanField(verbose_name="Twitter", default=True)

    logo = FilerImageField(
        verbose_name=_('Логотип'),
        on_delete=models.CASCADE,
        blank=True, null=True
    )
 
    def __str__(self):
        return 'Конфигурация сайта'

    def socials(self):
        return self.social_set.all()

    class Meta:
        verbose_name = "Конфигурация сайта"
        verbose_name_plural = "Конфигурация сайта"

class Social(models.Model):
    sitesettings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE,)
    text = models.CharField(verbose_name='Текст', help_text="Примеры: \"ВК\", \"Мы в контакте\", \"Мы в ВК\"", max_length=256, default="")
    url = models.URLField(verbose_name="Ссылка на страницу в соц.сети.")
    icon = models.CharField(verbose_name="Иконка соц.сети",
                                help_text='Названия иконок брать <a href="https://fontawesome.com/v4/icons/" target="blank">отсюда</a>', 
                                max_length=32, default="")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "соц.сеть"
        verbose_name_plural = "соц.сети"