from django.contrib import admin

from .models import (
    ContactMessage,
    CVSection,
    ExperienceItem,
    OfferItem,
    Person,
    PortfolioProject,
    PortfolioReference,
    SiteText,
)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    list_filter = ("created_at",)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "localized_title", "email")
    search_fields = ("first_name", "last_name", "title", "title_pl", "title_en", "email")


@admin.register(CVSection)
class CVSectionAdmin(admin.ModelAdmin):
    list_display = ("person", "type", "localized_title", "order")
    list_filter = ("type",)
    search_fields = ("title", "title_pl", "title_en", "content", "content_pl", "content_en")


@admin.register(ExperienceItem)
class ExperienceItemAdmin(admin.ModelAdmin):
    list_display = ("company", "localized_position", "start_date", "end_date")
    search_fields = (
        "company",
        "position",
        "position_pl",
        "position_en",
        "description",
        "description_pl",
        "description_en",
    )


@admin.register(PortfolioProject)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("localized_title", "localized_technologies", "project_url", "order")
    search_fields = (
        "title",
        "title_pl",
        "title_en",
        "description",
        "description_pl",
        "description_en",
        "technologies",
        "technologies_pl",
        "technologies_en",
    )
    list_editable = ("order",)


@admin.register(PortfolioReference)
class PortfolioReferenceAdmin(admin.ModelAdmin):
    list_display = ("title", "signature", "reference_png_url", "order")
    search_fields = ("title", "content", "signature", "reference_png_url")
    list_editable = ("order",)


@admin.register(OfferItem)
class OfferItemAdmin(admin.ModelAdmin):
    list_display = ("slot", "localized_title", "image_url")
    search_fields = (
        "title",
        "title_pl",
        "title_en",
        "content",
        "content_pl",
        "content_en",
        "image_url",
    )
    ordering = ("slot",)


@admin.register(SiteText)
class SiteTextAdmin(admin.ModelAdmin):
    list_display = ("key", "localized_value", "note")
    search_fields = ("key", "value_pl", "value_en", "note")
    ordering = ("key",)
