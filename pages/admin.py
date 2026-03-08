from django.contrib import admin
from .models import ContactMessage, PortfolioProject, CVSection, Person, ExperienceItem

admin.site.register(ContactMessage)
admin.site.register(Person)
admin.site.register(CVSection)
admin.site.register(ExperienceItem)

@admin.register(PortfolioProject)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'project_url')
    search_fields = ('title', 'technologies')