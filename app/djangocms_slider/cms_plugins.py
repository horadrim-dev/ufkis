from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from .models import Slider, Slide


class SlideInlineAdmin(admin.StackedInline):
    model = Slide
    extra = 0

@plugin_pool.register_plugin
class SliderPlugin(CMSPluginBase):
    model = Slider
    name = "Слайдер"
    render_template = "slider.html"
    cache = True
    inlines = (SlideInlineAdmin, )
    # fieldsets = (
    #     (None, {
    #         'fields': [
    #             'folder',
    #             ('pageThumbWidth',
    #             'pageThumbHeight',
    #             'pageThumbMarginVertical',
    #             'pageThumbMarginHorizontal',),
    #         ]
    #     }),
    #     (_('Toolbar Settings'), {
    #         'fields': [
    #             'zoomActualSize',
    #             'fullscreen',
    #             'zoom',
    #         ]
    #     }),
    # )

    def render(self, context, instance, placeholder):
        context.update({
            'id': instance.generate_id(),
            'slides': instance.get_slides(),
            # 'images': instance.get_folder_images(),
            # 'pageThumbWidthHeight': instance.parse_page_thumb_width_height(),
            # 'pageThumbMarginHorizontal': instance.pageThumbMarginHorizontal,
            # 'pageThumbMarginVertical': instance.pageThumbMarginVertical,
            # 'mode': instance.mode,
            # 'cssEasing': instance.cssEasing,
            # 'easing': instance.easing,
            # 'speed': instance.speed,
            # 'height': instance.height,
            # 'width': instance.width,
            # 'addClass': instance.addClass,
            # 'startClass': instance.startClass,
            # 'backdropDuration': instance.backdropDuration,
            # 'hideBarsDelay': instance.hideBarsDelay,
            # 'useLeft': instance.useLeft,
            # 'closable': instance.closable,
            # 'loop': instance.loop,
            # 'escKey': instance.escKey,
            # 'keyPress': instance.escKey,
            # 'controls': instance.controls,
            # 'slideEndAnimation': instance.slideEndAnimation,
            # 'hideControlOnEnd': instance.hideControlOnEnd,
            # 'mousewheel': instance.mousewheel,
            # 'preload': instance.preload,
            # 'showAfterLoad': instance.showAfterLoad,
            # 'nextHtml': instance.nextHtml,
            # 'index': instance.index,
            # 'iframeMaxWidth': instance.iframeMaxWidth,
            # 'download': instance.download,
            # 'counter': instance.counter,
            # 'appendCounterTo': instance.appendCounterTo,
            # 'swipeThreshold': instance.swipeThreshold,
            # 'enableDrag': instance.enableDrag,
            # 'enableSwipe': instance.enableSwipe,
            # 'thumbnails': instance.thumbnails,
            # 'animateThumb': instance.animateThumb,
            # 'currentPagerPosition': instance.currentPagerPosition,
            # 'thumbWidth': instance.thumbWidth,
            # 'thumbContHeight': instance.thumbContHeight,
            # 'thumbMargin': instance.thumbMargin,
            # 'showThumbByDefault': instance.showThumbByDefault,
            # 'toggleThumb': instance.toggleThumb,
            # 'pullCaptionUp': instance.pullCaptionUp,
            # 'enableThumbDrag': instance.enableThumbDrag,
            # 'enableThumbSwipe': instance.enableThumbSwipe,
            # 'id': instance.generate_id(),
            # 'fullscreen': instance.fullscreen,
            # 'zoom': instance.zoom,
            # 'zoomScale': instance.zoomScale,
            # 'zoomEnableZoomAfter': instance.zoomEnableZoomAfter,
            # 'zoomActualSize': instance.zoomActualSize,
            # 'pager': instance.pager,
            # 'hash': instance.hash,
            # 'galleryId': instance.galleryId,
            # 'share': instance.share,
            # 'facebook': instance.facebook,
            # 'facebookDropdownText': instance.facebookDropdownText,
            # 'twitter': instance.twitter,
            # 'twitterDropdownText': instance.twitterDropdownText,
            # 'googlePlus': instance.googlePlus,
            # 'googlePlusDropdownText': instance.googlePlusDropdownText,
            # 'pinterest': instance.pinterest,
            # 'pinterestDropdownText': instance.pinterestDropdownText,
        })
        return context

