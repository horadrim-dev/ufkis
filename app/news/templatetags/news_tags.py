from django import template

register = template.Library()


@register.filter
def prepare_tag_name(tagname:str):
    """
    return same string as filter
    example: "testtag" -> "testtag", "te st tag" -> "\"te+st+tag\""
    """
    arr = tagname.split(' ')
    if len(arr) == 1:
        return tagname
    else:
        return "\"{}\"".format('+'.join(arr))