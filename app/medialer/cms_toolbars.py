from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.extensions.toolbar import ExtensionToolbar
from cms.utils.urlutils import admin_reverse
from django.urls import reverse 


@toolbar_pool.register
class MedialerToolbar(CMSToolbar):

    def populate(self):


        # self.toolbar.add_sideframe_button(
        #     name='Новости', 
        #     url=admin_reverse('news_post_changelist'),
        #     )

        media_menu = self.toolbar.get_or_create_menu(
            key='medialer_cms_integration',
            verbose_name='Медиа'
        )
        media_menu .add_sideframe_item(
            name='Альбомы',
            url=admin_reverse('medialer_album_changelist')
        )

        self.toolbar.add_modal_button(
            name='+ фото в галерею', 
            url=admin_reverse('medialer_albumpicture_add'),
            # on_close=reverse('news:index')
            )