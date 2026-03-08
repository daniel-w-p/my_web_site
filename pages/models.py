from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Wiadomość kontaktowa"
        verbose_name_plural = "Wiadomości kontaktowe"

    def __str__(self):
        return f"{self.name} <{self.email}>"

class PortfolioProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200, blank=True)
    project_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='portfolio_images/', blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Projekt portfolio"
        verbose_name_plural = "Projekty portfolio"

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    photo = models.ImageField(upload_to="cv_photos/", default="static/img/cv_img.png")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Osoba CV"
        verbose_name_plural = "Osoby CV"

class CVSection(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="sections")

    SECTION_TYPES = [
        ("summary", "Podsumowanie"),
        ("experience", "Doświadczenie"),
        ("education", "Wykształcenie"),
        ("skills", "Umiejętności"),
        ("projects", "Projekty"),
        ("certificates", "Certyfikaty"),
        ("languages", "Języki"),
        ("other", "Inne"),
    ]
    type = models.CharField(max_length=50, choices=SECTION_TYPES)
    title = models.CharField(max_length=100)
    content = models.TextField()

    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Sekcja CV"
        verbose_name_plural = "Sekcje CV"

    def __str__(self):
        return f"{self.person}: {self.title}"

    @property
    def skills_list(self) -> list[str]:
        """
        Splits comma-separated skills, trims whitespace, drops empty items.
        Safe to use in templates: {% for s in section.skills_list %}.
        """
        if not self.content:
            return []
        return [s.strip() for s in self.content.split(",") if s.strip()]


class ExperienceItem(models.Model):
    section = models.ForeignKey(CVSection, on_delete=models.CASCADE, related_name="experience_items")
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["start_date"]