from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.extensions.toolbar import ExtensionToolbar
from cms.utils.urlutils import admin_reverse

@toolbar_pool.register
class NewsToolbar(CMSToolbar):

    def populate(self):

        menu = self.toolbar.get_or_create_menu(
            key='news_cms_integration',
            verbose_name='Новости'
        )
        menu.add_sideframe_item(
            name='Новости',
            url=admin_reverse('news_post_changelist')
        )
        menu.add_modal_item(
            name='Добавить новость',
            url=admin_reverse('news_post_add')
        )
        menu.add_modal_item(
            name='Категории',
            url=admin_reverse('news_category_changelist')
        )
        menu.add_modal_item(
            name='Добавить категорию',
            url=admin_reverse('news_category_add')
        )