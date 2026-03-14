from django.db import models
from django.templatetags.static import static
from django.utils.translation import get_language


def _localized_value(pl_value: str, en_value: str, fallback: str = "") -> str:
    lang = (get_language() or "pl").lower()
    primary, secondary = (en_value, pl_value) if lang.startswith("en") else (pl_value, en_value)
    return primary or secondary or fallback


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Wiadomosc kontaktowa"
        verbose_name_plural = "Wiadomosci kontaktowe"

    def __str__(self):
        return f"{self.name} <{self.email}>"


class PortfolioProject(models.Model):
    title = models.CharField(max_length=200)
    title_pl = models.CharField(max_length=200, blank=True)
    title_en = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    description_pl = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    technologies = models.CharField(max_length=200, blank=True)
    technologies_pl = models.CharField(max_length=200, blank=True)
    technologies_en = models.CharField(max_length=200, blank=True)
    project_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="portfolio_images/", blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]
        verbose_name = "Projekt portfolio"
        verbose_name_plural = "Projekty portfolio"

    @property
    def localized_title(self) -> str:
        return _localized_value(self.title_pl, self.title_en, self.title)

    @property
    def localized_description(self) -> str:
        return _localized_value(self.description_pl, self.description_en, self.description)

    @property
    def localized_technologies(self) -> str:
        return _localized_value(self.technologies_pl, self.technologies_en, self.technologies)

    @property
    def skills_list(self) -> list[str]:
        content = self.localized_technologies
        if not content:
            return []
        return [s.strip() for s in content.split(",") if s.strip()]


class PortfolioReference(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    reference_png_url = models.CharField(max_length=200, blank=True)
    signature = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Referencja portfolio"
        verbose_name_plural = "Referencje portfolio"

    def __str__(self):
        return self.title

    @property
    def reference_png_static_url(self) -> str:
        if not self.reference_png_url:
            return ""
        path = self.reference_png_url.strip()
        if path.startswith(("http://", "https://")):
            return path
        return static(path.lstrip("/"))


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=255, blank=True)
    title_pl = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=255, blank=True)
    location_pl = models.CharField(max_length=255, blank=True)
    location_en = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    photo = models.ImageField(upload_to="cv_photos/", default="static/img/cv_img.png")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Osoba CV"
        verbose_name_plural = "Osoby CV"

    @property
    def localized_title(self) -> str:
        return _localized_value(self.title_pl, self.title_en, self.title)

    @property
    def localized_location(self) -> str:
        return _localized_value(self.location_pl, self.location_en, self.location)


class CVSection(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="sections")

    SECTION_TYPES = [
        ("summary", "Podsumowanie"),
        ("experience", "Doswiadczenie"),
        ("education", "Wyksztalcenie"),
        ("skills", "Umiejetnosci"),
        ("techstack", "Stos technologiczny"),
        ("projects", "Projekty"),
        ("certificates", "Certyfikaty"),
        ("languages", "Jezyki"),
        ("other", "Inne"),
    ]
    type = models.CharField(max_length=50, choices=SECTION_TYPES)
    title = models.CharField(max_length=100)
    title_pl = models.CharField(max_length=100, blank=True)
    title_en = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    content_pl = models.TextField(blank=True)
    content_en = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Sekcja CV"
        verbose_name_plural = "Sekcje CV"

    def __str__(self):
        return f"{self.person}: {self.title}"

    @property
    def localized_title(self) -> str:
        return _localized_value(self.title_pl, self.title_en, self.title)

    @property
    def localized_content(self) -> str:
        return _localized_value(self.content_pl, self.content_en, self.content)

    @property
    def skills_list(self) -> list[str]:
        content = self.localized_content
        if not content:
            return []
        return [s.strip() for s in content.split(",") if s.strip()]


class ExperienceItem(models.Model):
    section = models.ForeignKey(CVSection, on_delete=models.CASCADE, related_name="experience_items")
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    position_pl = models.CharField(max_length=255, blank=True)
    position_en = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    description_pl = models.TextField(blank=True)
    description_en = models.TextField(blank=True)

    class Meta:
        ordering = ["start_date"]

    @property
    def localized_position(self) -> str:
        return _localized_value(self.position_pl, self.position_en, self.position)

    @property
    def localized_description(self) -> str:
        return _localized_value(self.description_pl, self.description_en, self.description)


class SiteText(models.Model):
    key = models.CharField(max_length=120, unique=True)
    value_pl = models.TextField(blank=True)
    value_en = models.TextField(blank=True)
    note = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["key"]
        verbose_name = "Tekst strony"
        verbose_name_plural = "Teksty strony"

    def __str__(self):
        return self.key

    @property
    def localized_value(self) -> str:
        return _localized_value(self.value_pl, self.value_en)

