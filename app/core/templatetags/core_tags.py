from django import template

register = template.Library()


STYLE_CHOICES = ('all_in_one', 'list')
SIZE_CHOICES = ('small', 'medium', 'large')
BORDER_CHOICES = ('none', 'square', 'circle')
@register.inclusion_tag("core/includes/share_buttons.html", takes_context=True)
def render_share_buttons(context, url, title, description=None, image_path=None, 
                          size="medium", border="circle", style="all_in_one"):
    """
    Render social buttons for sharing
    """
    socials = []
    if context['site_settings'].share_vk:
        socials.append(('vk', 'ВКонтакте'))
    if context['site_settings'].share_ok:
        socials.append(('odnoklassniki', 'Одноклассники'))
    if context['site_settings'].share_fb:
        socials.append(('facebook', 'Facebook'))
    if context['site_settings'].share_twitter:
        socials.append(('twitter', 'Twitter'))
    if context['site_settings'].share_instagram:
        socials.append(('instagram', 'Instagram'))

    return {
        "url": url,
        "title": title,
        "description": description,
        "image_path": image_path,
        'size': size if size in SIZE_CHOICES else None,
        'border': border if border in BORDER_CHOICES else None,
        'style': style if style in STYLE_CHOICES else None,
        'socials': socials,
    }


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/

    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.

    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.

    For example, if you're on the page ``/things/?with_frosting=true&page=5``,
    then

    <a href="/things/?{% param_replace page=3 %}">Page 3</a>

    would expand to

    <a href="/things/?with_frosting=true&page=3">Page 3</a>

    Based on
    https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()

