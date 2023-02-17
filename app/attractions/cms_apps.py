from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class AttractionsApphook(CMSApp):
    app_name = "attractions"  # must match the application namespace
    name = "Attractions Apphook"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["attractions.urls"] # replace this with the path to your application's URLs module