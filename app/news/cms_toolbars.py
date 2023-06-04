from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.extensions.toolbar import ExtensionToolbar
from cms.utils.urlutils import admin_reverse
from django.urls import reverse 
@toolbar_pool.register
class NewsToolbar(CMSToolbar):

    def populate(self):


        # self.toolbar.add_sideframe_button(
        #     name='Новости', 
        #     url=admin_reverse('news_post_changelist'),
        #     )

        news_menu = self.toolbar.get_or_create_menu(
            key='news_cms_integration',
            verbose_name='Новости'
        )
        news_menu .add_sideframe_item(
            name='Новости',
            url=admin_reverse('news_post_changelist')
        )
        news_menu.add_modal_item(
            name='Добавить новость',
            url=admin_reverse('news_post_add'), 
            on_close=reverse('news:index')
        )
        news_menu.add_modal_item(
            name='Категории',
            url=admin_reverse('news_category_changelist')
        )
        news_menu.add_modal_item(
            name='Добавить категорию',
            url=admin_reverse('news_category_add')
        )

        tags_menu = self.toolbar.get_or_create_menu(
            key='taggit_cms_integration',
            verbose_name='Теги'
        )
        tags_menu .add_sideframe_item(
            name='Теги',
            url=admin_reverse('taggit_tag_changelist')
        )
        self.toolbar.add_modal_button(
            name='Добавить новость', 
            url=admin_reverse('news_post_add'),
            on_close=reverse('news:index')
            )
        self.toolbar.add_modal_button(
            name='Добавить тег', 
            url=admin_reverse('taggit_tag_add'),
            )