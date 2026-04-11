from urllib.parse import urlparse
from urllib.parse import urlsplit, urlunsplit
import re

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string

from pages.forms import ContactMessageForm
from pages.models import CVSection, OfferItem, Person, PortfolioProject, PortfolioReference
from pages.utils import get_site_text


# from weasyprint import HTML


def _split_parenthetical_tags(value: str) -> tuple[str, list[str]]:
    text = (value or "").rstrip()
    if not text:
        return "", []

    trailing = re.search(r"(?:\s*\([^()]+\)\s*)+$", text)
    if not trailing:
        return text, []

    trailing_part = trailing.group(0)
    tags = [tag.strip() for tag in re.findall(r"\(([^()]+)\)", trailing_part) if tag.strip()]
    cleaned = text[: trailing.start()].rstrip()
    return cleaned, tags


def index(request):
    person = Person.objects.prefetch_related("sections").order_by("id").first()
    tech_sections = []
    cert_sections = []

    if person:
        source_sections = person.sections.filter(type="techstack").order_by("order", "id")
        tech_sections = [
            {
                "title": section.localized_title,
                "items": section.skills_list,
            }
            for section in source_sections
        ]

        source_cert_sections = person.sections.filter(type="certificates").order_by("order", "id")
        cert_sections = [
            {
                "title": profile.title,
                "link": profile.content,
            }
            for profile in source_cert_sections
        ]

    return render(request, "index.html", {"tech_sections": tech_sections, "cert_sections": cert_sections})


def portfolio(request):
    projects = PortfolioProject.objects.order_by("order", "id")
    references = PortfolioReference.objects.order_by("order", "id")
    return render(request, "portfolio.html", {"projects": projects, "references": references})


def offer(request):
    cards_by_slot = {item.slot: item for item in OfferItem.objects.order_by("slot", "id")}
    offer_cards = [cards_by_slot.get(slot) for slot in range(1, 5)]
    return render(request, "offer.html", {"offer_cards": offer_cards})


def contact(request):
    saved = False

    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
            form = ContactMessageForm()
    else:
        form = ContactMessageForm()

    return render(request, "contact.html", {"form": form, "saved": saved})


def privacy_policy(request):
    return render(request, "privacy_policy.html")


def cv_view(request, person_id=1):
    person = get_object_or_404(Person, pk=person_id)
    sections = person.sections.prefetch_related("experience_items").order_by("order", "id")
    headings = {
        "experience": get_site_text("cv.heading.experience", "Doswiadczenie"),
        "education": get_site_text("cv.heading.education", "Edukacja"),
        "tech": get_site_text("cv.heading.tech", "Technologie i umiejetnosci"),
        "certificates": get_site_text("cv.heading.certificates", "Certyfikaty i profile"),
        "languages": get_site_text("cv.heading.languages", "Jezyki"),
        "other": get_site_text("cv.heading.other", "Pozostale"),
        "empty": get_site_text("cv.empty", "Brak danych CV do wyswietlenia."),
    }

    summary_sections = []
    tech_sections = []
    certificate_sections = []
    language_sections = []
    experience_entries = []
    education_entries = []
    other_sections = []

    for section in sections:
        localized_title = section.localized_title
        localized_content = section.localized_content

        if section.type == "summary":
            summary_sections.append(section)
            continue

        if section.type in {"techstack", "skills"}:
            items = section.skills_list
            if items:
                tech_sections.append({"title": localized_title, "items": items})
            elif localized_content:
                tech_sections.append({"title": localized_title, "items": [localized_content]})
            continue

        if section.type == "certificates":
            raw_link = localized_content.strip()
            parsed = urlparse(raw_link)
            is_url = bool(parsed.scheme and parsed.netloc)
            certificate_sections.append(
                {
                    "title": localized_title,
                    "link": raw_link,
                    "is_url": is_url,
                }
            )
            continue

        if section.type == "experience":
            items = section.experience_items.all()
            if items:
                for item in items:
                    position_text, position_tags = _split_parenthetical_tags(item.localized_position)
                    description_text, description_tags = _split_parenthetical_tags(item.localized_description)
                    experience_entries.append(
                        {
                            "section_title": localized_title,
                            "position": position_text or localized_title,
                            "position_tags": position_tags,
                            "company": item.company,
                            "start_date": item.start_date,
                            "end_date": item.end_date,
                            "description": description_text,
                            "description_tags": description_tags,
                        }
                    )
            elif localized_content:
                fallback_desc, fallback_tags = _split_parenthetical_tags(localized_content)
                experience_entries.append(
                    {
                        "section_title": localized_title,
                        "position": localized_title,
                        "position_tags": [],
                        "company": "",
                        "start_date": None,
                        "end_date": None,
                        "description": fallback_desc,
                        "description_tags": fallback_tags,
                    }
                )
            continue

        if section.type == "education":
            items = section.experience_items.all()
            if items:
                for item in items:
                    education_entries.append(
                        {
                            "title": item.localized_position,
                            "institution": item.company,
                            "start_date": item.start_date,
                            "end_date": item.end_date,
                            "description": item.localized_description,
                        }
                    )
            else:
                education_entries.append(
                    {
                        "title": localized_title,
                        "institution": "",
                        "start_date": None,
                        "end_date": None,
                        "description": localized_content,
                    }
                )
            continue

        if section.type == "languages":
            language_sections.append(section)
            continue

        other_sections.append(section)

    return render(
        request,
        "cv.html",
        {
            "person": person,
            "today_label": get_site_text("cv.today", "today"),
            "summary_sections": summary_sections,
            "tech_sections": tech_sections,
            "certificate_sections": certificate_sections,
            "language_sections": language_sections,
            "experience_entries": experience_entries,
            "education_entries": education_entries,
            "other_sections": other_sections,
            "cv_headings": headings,
        },
    )


def switch_language(request):
    if request.method != "POST":
        return redirect("index")

    allowed = {code for code, _ in settings.LANGUAGES}
    default_lang = settings.LANGUAGE_CODE
    lang = request.POST.get("language", default_lang)
    if lang not in allowed:
        lang = default_lang

    next_url = request.POST.get("next") or "/"
    parsed = urlsplit(next_url)
    path = parsed.path or "/"
    if not path.startswith("/"):
        path = f"/{path}"

    for code, _ in settings.LANGUAGES:
        pref = f"/{code}/"
        root_pref = f"/{code}"
        if path.startswith(pref):
            path = f"/{path[len(pref):]}"
            break
        if path == root_pref:
            path = "/"
            break

    if lang != default_lang:
        path = f"/{lang}{path}" if path != "/" else f"/{lang}/"

    redirect_url = urlunsplit(("", "", path, parsed.query, parsed.fragment))
    response = redirect(redirect_url)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response


def cv_pdf_view(request):
    sections = CVSection.objects.all()
    html_string = render_to_string("cv_pdf.html", {"sections": sections})

    # pdf_file = HTML(string=html_string).write_pdf()
    # response = HttpResponse(pdf_file, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="CV_ITechMind.pdf"'
    # return response
    return HttpResponse(html_string)
