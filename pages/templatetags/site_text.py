from django import template

from pages.utils import get_site_text

register = template.Library()


@register.simple_tag
def site_text(key: str, default: str = "") -> str:
    return get_site_text(key, default)
