from django.db import migrations, models


REFERENCE_SITE_TEXTS = [
    (
        "portfolio.references_heading",
        "Referencje",
        "References",
        "Portfolio references section heading",
    ),
    (
        "portfolio.references_cta",
        "Zobacz list referencyjny (PNG)",
        "View reference letter (PNG)",
        "Portfolio reference file button",
    ),
    (
        "portfolio.references_empty",
        "Brak referencji.",
        "No references yet.",
        "Portfolio references empty state",
    ),
]


def add_reference_site_texts(apps, schema_editor):
    SiteText = apps.get_model("pages", "SiteText")
    for key, value_pl, value_en, note in REFERENCE_SITE_TEXTS:
        SiteText.objects.update_or_create(
            key=key,
            defaults={"value_pl": value_pl, "value_en": value_en, "note": note},
        )


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0005_alter_cvsection_type_add_techstack"),
    ]

    operations = [
        migrations.CreateModel(
            name="PortfolioReference",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("reference_png_url", models.CharField(max_length=200, blank=True)),
                ("signature", models.CharField(max_length=255)),
                ("order", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Referencja portfolio",
                "verbose_name_plural": "Referencje portfolio",
                "ordering": ["order", "id"],
            },
        ),
        migrations.RunPython(add_reference_site_texts, migrations.RunPython.noop),
    ]
