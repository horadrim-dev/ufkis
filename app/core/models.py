from django.db import models, transaction
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

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