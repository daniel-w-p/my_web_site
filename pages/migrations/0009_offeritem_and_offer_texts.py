from django.db import migrations, models


OFFER_SITE_TEXTS = [
    ("nav.offer", "Oferta", "Offer", "Navbar item"),
    ("offer.page_title", "Oferta", "Offer", "Offer page title"),
    ("offer.heading", "Oferta", "Offer", "Offer page heading"),
    (
        "offer.subtitle",
        "Jak moge wesprzec Twoj projekt.",
        "How I can support your project.",
        "Offer page subtitle",
    ),
    (
        "offer.empty_title",
        "Pozycja oferty do uzupelnienia",
        "Offer item to be completed",
        "Offer empty state title",
    ),
    (
        "offer.empty_body",
        "Dodaj tresc i obraz tej karty w panelu administratora.",
        "Add content and image for this card in the admin panel.",
        "Offer empty state body",
    ),
    (
        "offer.meta_description",
        "Zakres uslug i modele wspolpracy w obszarze AI oraz Python/Django.",
        "Service scope and collaboration models in AI and Python/Django.",
        "SEO description",
    ),
]


DEFAULT_OFFER_ITEMS = [
    (
        1,
        "Konsultacje AI i analiza potrzeb",
        "Konsultacje AI i analiza potrzeb",
        "AI consulting and needs analysis",
        (
            "Warsztat i audyt procesow biznesowych, aby wskazac obszary, "
            "w ktorych AI przyniesie realny zwrot."
        ),
        (
            "Warsztat i audyt procesow biznesowych, aby wskazac obszary, "
            "w ktorych AI przyniesie realny zwrot."
        ),
        (
            "Workshops and business process audits to identify areas "
            "where AI delivers measurable value."
        ),
        "img/ai_consulting.png",
    ),
    (
        2,
        "Dedykowani agenci AI z RAG",
        "Dedykowani agenci AI z RAG",
        "Custom AI agents with RAG",
        (
            "Tworzenie dedykowanych agentow AI z RAG, integrujacych modele jezykowe z wiedza firmowa, dokumentami i procesami. "
            "Realizuje wdrozenia chmurowe oraz on-premise, z naciskiem na bezpieczenstwo, kontrole nad danymi i gotowosc enterprise. "
            "Posiadam takze zaplecze sprzetowe do lokalnego uruchamiania i testowania modeli."
        ),
        (
            "Tworzenie dedykowanych agentow AI z RAG, integrujacych modele jezykowe z wiedza firmowa, dokumentami i procesami. "
            "Realizuje wdrozenia chmurowe oraz on-premise, z naciskiem na bezpieczenstwo, kontrole nad danymi i gotowosc enterprise. "
            "Posiadam takze zaplecze sprzetowe do lokalnego uruchamiania i testowania modeli."
        ),
        (
            "Development of custom AI agents with RAG, integrating language models with company knowledge, documents, and workflows. "
            "I deliver both cloud and on-premise deployments with a strong focus on security, data control, and enterprise readiness. "
            "I also have the hardware resources required to run and test models locally."
        ),
        "img/ai_rag.png",
    ),
    (
        3,
        "Aplikacje webowe Python/Django",
        "Aplikacje webowe Python/Django",
        "Python/Django web applications",
        (
            "Projektowanie i wdrazanie bezpiecznych aplikacji webowych "
            "dopasowanych do procesow firmy."
        ),
        (
            "Projektowanie i wdrazanie bezpiecznych aplikacji webowych "
            "dopasowanych do procesow firmy."
        ),
        (
            "Design and delivery of secure web applications "
            "aligned with company workflows."
        ),
        "img/backend.png",
    ),
    (
        4,
        "Automatyzacje i integracje",
        "Automatyzacje i integracje",
        "Automation and integrations",
        (
            "Automatyzacja powtarzalnych zadan oraz laczenie narzedzi "
            "w jeden przewidywalny przeplyw pracy."
        ),
        (
            "Automatyzacja powtarzalnych zadan oraz laczenie narzedzi "
            "w jeden przewidywalny przeplyw pracy."
        ),
        (
            "Automation of repetitive tasks and connecting tools "
            "into one reliable workflow."
        ),
        "img/automation.png",
    ),
]


def seed_offer_content(apps, schema_editor):
    SiteText = apps.get_model("pages", "SiteText")
    OfferItem = apps.get_model("pages", "OfferItem")

    for key, value_pl, value_en, note in OFFER_SITE_TEXTS:
        SiteText.objects.update_or_create(
            key=key,
            defaults={"value_pl": value_pl, "value_en": value_en, "note": note},
        )

    for slot, title, title_pl, title_en, content, content_pl, content_en, image_url in DEFAULT_OFFER_ITEMS:
        OfferItem.objects.update_or_create(
            slot=slot,
            defaults={
                "title": title,
                "title_pl": title_pl,
                "title_en": title_en,
                "content": content,
                "content_pl": content_pl,
                "content_en": content_en,
                "image_url": image_url,
            },
        )


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0008_add_meta_site_texts"),
    ]

    operations = [
        migrations.CreateModel(
            name="OfferItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slot", models.PositiveSmallIntegerField(choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4")], unique=True)),
                ("title", models.CharField(max_length=200)),
                ("title_pl", models.CharField(blank=True, max_length=200)),
                ("title_en", models.CharField(blank=True, max_length=200)),
                ("content", models.TextField()),
                ("content_pl", models.TextField(blank=True)),
                ("content_en", models.TextField(blank=True)),
                ("image_url", models.CharField(blank=True, max_length=255)),
            ],
            options={
                "verbose_name": "Element oferty",
                "verbose_name_plural": "Elementy oferty",
                "ordering": ["slot", "id"],
            },
        ),
        migrations.RunPython(seed_offer_content, migrations.RunPython.noop),
    ]
