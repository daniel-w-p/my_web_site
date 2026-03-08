from django.utils.translation import get_language

from .models import SiteText


def get_site_text(key: str, default: str = "") -> str:
    try:
        entry = SiteText.objects.get(key=key)
    except SiteText.DoesNotExist:
        return default

    lang = (get_language() or "pl").lower()
    if lang.startswith("en"):
        return entry.value_en or entry.value_pl or default
    return entry.value_pl or entry.value_en or default
