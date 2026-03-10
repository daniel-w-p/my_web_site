from urllib.parse import urlsplit, urlunsplit

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string

from pages.forms import ContactMessageForm
from pages.models import CVSection, Person, PortfolioProject
from pages.utils import get_site_text


# from weasyprint import HTML


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

    return render(request, "index.html",
                  {"tech_sections": tech_sections, "cert_sections": cert_sections})


def portfolio(request):
    projects = PortfolioProject.objects.order_by("order", "id")
    return render(request, "portfolio.html", {"projects": projects})


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


def cv_view(request, person_id=1):
    person = get_object_or_404(Person, pk=person_id)
    sections = person.sections.prefetch_related("experience_items").all()
    return render(
        request,
        "cv.html",
        {
            "person": person,
            "sections": sections,
            "today_label": get_site_text("cv.today", "today"),
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

