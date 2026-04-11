"""
URL configuration for mysite project.
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

from pages import views

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("set-language/", views.switch_language, name="switch_language"),
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("offer/", views.offer, name="offer"),
    path("contact/", views.contact, name="contact"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("cv/", views.cv_view, name="cv"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    prefix_default_language=False,
)
