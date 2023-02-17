# from cms.menu_bases import CMSAttachMenu
# from django.utils.translation import ugettext_lazy as _
# from menus.base import NavigationNode
# from menus.menu_pool import menu_pool

# from .models import Attraction


# class AttractionsSubMenu(CMSAttachMenu):

#   name = _("Меню \"Аттракционы\"")

#   def get_nodes(self, request):

#     nodes = []
#     for obj in Attraction.objects.all():

#       node = NavigationNode(
#         obj.title,
#         obj.get_absolute_url(),
#         obj.pk
#       )
#       nodes.append(node)

#     return nodes

# menu_pool.register_menu(AttractionsSubMenu)