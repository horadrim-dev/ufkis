from menus.base import Modifier
from menus.menu_pool import menu_pool

from cms.models import Page

class IconModifier(Modifier):
    """
    This modifier makes the fa_icon attribute of a page
    accessible for the menu system.
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        # only do something when the menu has already been cut
        if post_cut:
            # only consider nodes that refer to cms pages
            # and put them in a dict for efficient access
            page_nodes = {n.id: n for n in nodes if n.attr["is_page"]}
            # retrieve the attributes of interest from the relevant pages
            pages = Page.objects.filter(id__in=page_nodes.keys())#.values('id', 'iconextension')
            # loop over all relevant pages
            # assert False, page_nodes
            # hz = [x['iconextension'] for x in pages]
            for page in pages:
                # take the node referring to the page
                node = page_nodes[page.id]
                # put the changed_by attribute on the node
                node.attr["icon"] = page.iconextension.fa_icon

        return nodes

menu_pool.register_modifier(IconModifier)