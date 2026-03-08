from django.db import migrations, models


DEFAULT_SITE_TEXTS = [
    ("nav.about", "O mnie", "About", "Navbar item"),
    ("nav.services", "Uslugi", "Services", "Navbar item"),
    ("nav.portfolio", "Portfolio", "Portfolio", "Navbar item"),
    ("nav.contact", "Kontakt", "Contact", "Navbar item"),
    ("nav.cv", "CV", "CV", "Navbar item"),
    (
        "index.meta_title",
        "ITechMind - Specjalista AI i Developer",
        "ITechMind - AI Specialist and Developer",
        "Home meta title",
    ),
    ("index.hero_title", "Czesc! Tu ITechMind", "Hello! This is ITechMind", "Home hero title"),
    (
        "index.hero_subtitle",
        "Specjalista AI i Python / Django Developer",
        "AI Specialist and Python / Django Developer",
        "Home hero subtitle",
    ),
    (
        "index.hero_description",
        "Pomagam tworzyc nowoczesne systemy IT i rozwiazania oparte na sztucznej inteligencji.",
        "I help build modern IT systems and AI-powered solutions.",
        "Home hero description",
    ),
    ("index.hero_cta", "Zobacz projekty", "See projects", "Home hero button"),
    ("index.about_title", "O mnie", "About me", "Home about title"),
    (
        "index.about_body",
        "Krotki opis doswiadczenia, kompetencji i wartosci dla klienta.",
        "Short description of your experience, strengths and value for clients.",
        "Home about body",
    ),
    ("index.services_title", "Co robie", "What I do", "Home services title"),
    ("index.service_1_title", "AI i ML Consulting", "AI and ML Consulting", "Service card title"),
    (
        "index.service_1_body",
        "Konsultacje, prototypy i strategie AI dopasowane do biznesu.",
        "Consulting, prototypes and practical AI strategy for business.",
        "Service card body",
    ),
    ("index.service_2_title", "Backend (Python/Django)", "Backend (Python/Django)", "Service card title"),
    (
        "index.service_2_body",
        "Budowa backendow i API o wysokiej jakosci i bezpieczenstwie.",
        "Building high-quality, secure backends and APIs.",
        "Service card body",
    ),
    (
        "index.service_3_title",
        "Web Apps i Automatyzacje",
        "Web Apps and Automation",
        "Service card title",
    ),
    (
        "index.service_3_body",
        "Aplikacje webowe, integracje i systemy automatyzujace prace.",
        "Web applications, integrations and workflow automation.",
        "Service card body",
    ),
    ("portfolio.page_title", "Portfolio", "Portfolio", "Portfolio page title"),
    ("portfolio.heading", "Portfolio", "Portfolio", "Portfolio heading"),
    ("portfolio.cta_project", "Zobacz projekt", "View project", "Portfolio button"),
    (
        "portfolio.empty",
        "Brak projektow w portfolio.",
        "No portfolio projects yet.",
        "Portfolio empty state",
    ),
    ("contact.page_title", "Kontakt", "Contact", "Contact page title"),
    ("contact.heading", "Skontaktuj sie", "Get in touch", "Contact heading"),
    (
        "contact.success",
        "Twoja wiadomosc zostala zapisana. Dziekuje za kontakt.",
        "Your message has been saved. Thank you for reaching out.",
        "Contact success message",
    ),
    (
        "contact.label_name",
        "Imie i nazwisko lub nazwa firmy",
        "Name or company",
        "Contact form label",
    ),
    ("contact.label_email", "Adres e-mail", "Email address", "Contact form label"),
    ("contact.label_message", "Wiadomosc", "Message", "Contact form label"),
    ("contact.submit", "Wyslij", "Send", "Contact form button"),
    ("cv.page_title", "CV", "CV", "CV page title"),
    ("cv.today", "dzis", "today", "CV open-ended date label"),
    ("quick_contact.title", "Szybki kontakt", "Quick contact", "Quick contact section title"),
    ("quick_contact.email_label", "Email", "Email", "Quick contact item label"),
    ("quick_contact.phone_label", "Telefon", "Phone", "Quick contact item label"),
    ("quick_contact.email_href", "kontakt@itechmind.pl", "contact@itechmind.pl", "Quick contact email target"),
    ("quick_contact.phone_href", "+48123456789", "+48123456789", "Quick contact phone target"),
    ("quick_contact.github_href", "https://github.com/your-profile", "https://github.com/your-profile", "Quick contact GitHub URL"),
    ("quick_contact.linkedin_href", "https://www.linkedin.com/in/your-profile/", "https://www.linkedin.com/in/your-profile/", "Quick contact LinkedIn URL"),
]


def fill_translations_and_site_texts(apps, schema_editor):
    PortfolioProject = apps.get_model("pages", "PortfolioProject")
    Person = apps.get_model("pages", "Person")
    CVSection = apps.get_model("pages", "CVSection")
    ExperienceItem = apps.get_model("pages", "ExperienceItem")
    SiteText = apps.get_model("pages", "SiteText")

    for project in PortfolioProject.objects.all():
        if not project.title_pl:
            project.title_pl = project.title
        if not project.title_en:
            project.title_en = project.title
        if not project.description_pl:
            project.description_pl = project.description
        if not project.description_en:
            project.description_en = project.description
        if not project.technologies_pl:
            project.technologies_pl = project.technologies
        if not project.technologies_en:
            project.technologies_en = project.technologies
        project.save()

    for person in Person.objects.all():
        if not person.title_pl:
            person.title_pl = person.title
        if not person.title_en:
            person.title_en = person.title
        if not person.location_pl:
            person.location_pl = person.location
        if not person.location_en:
            person.location_en = person.location
        person.save()

    for section in CVSection.objects.all():
        if not section.title_pl:
            section.title_pl = section.title
        if not section.title_en:
            section.title_en = section.title
        if not section.content_pl:
            section.content_pl = section.content
        if not section.content_en:
            section.content_en = section.content
        section.save()

    for item in ExperienceItem.objects.all():
        if not item.position_pl:
            item.position_pl = item.position
        if not item.position_en:
            item.position_en = item.position
        if not item.description_pl:
            item.description_pl = item.description
        if not item.description_en:
            item.description_en = item.description
        item.save()

    for key, value_pl, value_en, note in DEFAULT_SITE_TEXTS:
        SiteText.objects.update_or_create(
            key=key,
            defaults={"value_pl": value_pl, "value_en": value_en, "note": note},
        )


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0003_cvsection_person_experienceitem_cvsection_person"),
    ]

    operations = [
        migrations.AddField(
            model_name="cvsection",
            name="content_en",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="cvsection",
            name="content_pl",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="cvsection",
            name="title_en",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="cvsection",
            name="title_pl",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="experienceitem",
            name="description_en",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="experienceitem",
            name="description_pl",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="experienceitem",
            name="position_en",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="experienceitem",
            name="position_pl",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="person",
            name="location_en",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="person",
            name="location_pl",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="person",
            name="title_en",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="person",
            name="title_pl",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="portfolioproject",
            name="description_en",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="portfolioproject",
            name="description_pl",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="portfolioproject",
            name="technologies_en",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="portfolioproject",
            name="technologies_pl",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="portfolioproject",
            name="title_en",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="portfolioproject",
            name="title_pl",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name="SiteText",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("key", models.CharField(max_length=120, unique=True)),
                ("value_pl", models.TextField(blank=True)),
                ("value_en", models.TextField(blank=True)),
                ("note", models.CharField(blank=True, max_length=255)),
            ],
            options={
                "verbose_name": "Tekst strony",
                "verbose_name_plural": "Teksty strony",
                "ordering": ["key"],
            },
        ),
        migrations.RunPython(fill_translations_and_site_texts, migrations.RunPython.noop),
    ]


