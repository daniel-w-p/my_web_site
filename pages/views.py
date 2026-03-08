from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from pages.models import PortfolioProject, CVSection, Person
from pages.forms import ContactMessageForm
# from weasyprint import HTML

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    projects = PortfolioProject.objects.order_by('id')  # posortowane np. wg ID
    return render(request, "portfolio.html", {"projects": projects})

def contact(request):
    saved = False

    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()  # zapis do DB
            saved = True  # możemy potem pokazać komunikat
            form = ContactMessageForm()  # wyczyść formularz

    else:
        form = ContactMessageForm()

    return render(request, "contact.html", {"form": form, "saved": saved})

def cv_view(request, person_id=1):
    person = Person.objects.get(pk=person_id)
    sections = person.sections.prefetch_related("experience_items").all()
    print(sections)
    return render(request, "cv.html", {"person": person, "sections": sections})


def cv_pdf_view(request):
    sections = CVSection.objects.all()
    html_string = render_to_string('cv_pdf.html', {'sections': sections})

    # pdf_file = HTML(string=html_string).write_pdf()

    # response = HttpResponse(pdf_file, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="CV_ITechMind.pdf"'
    # return response
    pass