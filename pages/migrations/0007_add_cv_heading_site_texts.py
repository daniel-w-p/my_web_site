from django.db import migrations


CV_HEADING_SITE_TEXTS = [
    ("cv.heading.experience", "Doswiadczenie", "Experience", "CV heading"),
    ("cv.heading.education", "Edukacja", "Education", "CV heading"),
    ("cv.heading.tech", "Technologie i umiejetnosci", "Technologies and skills", "CV heading"),
    ("cv.heading.certificates", "Certyfikaty i profile", "Certificates and profiles", "CV heading"),
    ("cv.heading.languages", "Jezyki", "Languages", "CV heading"),
    ("cv.heading.other", "Pozostale", "Other", "CV heading"),
    ("cv.empty", "Brak danych CV do wyswietlenia.", "No CV data to display.", "CV empty state"),
]


def add_cv_heading_site_texts(apps, schema_editor):
    SiteText = apps.get_model("pages", "SiteText")
    for key, value_pl, value_en, note in CV_HEADING_SITE_TEXTS:
        SiteText.objects.update_or_create(
            key=key,
            defaults={"value_pl": value_pl, "value_en": value_en, "note": note},
        )


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0006_portfolioreference"),
    ]

    operations = [
        migrations.RunPython(add_cv_heading_site_texts, migrations.RunPython.noop),
    ]
