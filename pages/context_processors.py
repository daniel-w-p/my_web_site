from django.templatetags.static import static

from pages.utils import get_site_text


def seo_meta(request):
    url_name = getattr(getattr(request, "resolver_match", None), "url_name", "") or "index"

    title_by_view = {
        "index": get_site_text("index.hero_subtitle", "ITechMind - AI Specialist and Developer"),
        "portfolio": get_site_text("portfolio.page_title", "Portfolio"),
        "contact": get_site_text("contact.page_title", "Contact"),
        "cv": get_site_text("cv.page_title", "CV"),
        "privacy_policy": get_site_text("cookies.more", "Privacy Policy"),
    }
    description_by_view = {
        "index": get_site_text(
            "index.meta_description",
            "Portfolio, CV and contact page for AI and Python/Django development services.",
        ),
        "portfolio": get_site_text(
            "portfolio.meta_description",
            "Portfolio projects, implementations and references.",
        ),
        "contact": get_site_text(
            "contact.meta_description",
            "Contact form for project inquiries and cooperation.",
        ),
        "cv": get_site_text(
            "cv.meta_description",
            "Professional CV, experience, education, technologies and certificates.",
        ),
        "privacy_policy": get_site_text(
            "privacy.meta_description",
            "Privacy policy and information about essential cookies.",
        ),
    }

    seo_title = title_by_view.get(url_name, title_by_view["index"])
    seo_description = description_by_view.get(url_name, description_by_view["index"])
    base_url = f"{request.scheme}://{request.get_host()}"
    seo_url = f"{base_url}{request.path}"
    seo_image = f"{base_url}{static('img/logo.png')}"
    lang = (getattr(request, "LANGUAGE_CODE", "") or "pl").lower()
    og_locale = "en_US" if lang.startswith("en") else "pl_PL"

    return {
        "seo_title": seo_title,
        "seo_description": seo_description,
        "seo_url": seo_url,
        "seo_image": seo_image,
        "seo_site_name": get_site_text("meta.site_name", "ITechMind"),
        "seo_og_locale": og_locale,
    }
