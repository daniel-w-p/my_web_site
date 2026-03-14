from django.db import migrations


META_SITE_TEXTS = [
    ("meta.site_name", "ITechMind", "ITechMind", "SEO site name"),
    (
        "index.meta_description",
        "Portfolio, CV i kontakt dla uslug AI oraz Python/Django.",
        "Portfolio, CV and contact page for AI and Python/Django development services.",
        "SEO description",
    ),
    (
        "portfolio.meta_description",
        "Projekty portfolio, realizacje i referencje.",
        "Portfolio projects, implementations and references.",
        "SEO description",
    ),
    (
        "contact.meta_description",
        "Formularz kontaktowy do zapytan projektowych i wspolpracy.",
        "Contact form for project inquiries and cooperation.",
        "SEO description",
    ),
    (
        "cv.meta_description",
        "CV zawodowe: doswiadczenie, edukacja, technologie i certyfikaty.",
        "Professional CV: experience, education, technologies and certificates.",
        "SEO description",
    ),
    (
        "privacy.meta_description",
        "Polityka prywatnosci i informacje o niezbednych plikach cookie.",
        "Privacy policy and information about essential cookies.",
        "SEO description",
    ),
]


def add_meta_site_texts(apps, schema_editor):
    SiteText = apps.get_model("pages", "SiteText")
    for key, value_pl, value_en, note in META_SITE_TEXTS:
        SiteText.objects.update_or_create(
            key=key,
            defaults={"value_pl": value_pl, "value_en": value_en, "note": note},
        )


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0007_add_cv_heading_site_texts"),
    ]

    operations = [
        migrations.RunPython(add_meta_site_texts, migrations.RunPython.noop),
    ]
