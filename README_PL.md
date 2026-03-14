# ITechMind - portfolio site (Django)

Prosty serwis portfolio/CV z formularzem kontaktowym, zbudowany w Django.

Wersja angielska: `README.md`.

## Funkcje

- Strona główna (`/`)
- Strona portfolio (`/portfolio/`)
- Formularz kontaktowy zapisujący wiadomości w bazie danych (`/contact/`)
- Widok CV oparty o modele danych (`/cv/`)
- Panel administratora Django (`/admin/`)
- Wstępna konfiguracja internacjonalizacji (PL/EN)

## Technologie

- Python 3.12+
- Django 6.x
- SQLite (domyślna baza lokalna)

## Virtual Environment (venv)

Utwórz i aktywuj środowisko wirtualne:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Quick Start (Local)

1. Zainstaluj zależności.

```powershell
pip install -r requirements.txt
```

2. Uruchom migracje.

```powershell
python manage.py migrate
```

3. (Opcjonalnie) Dodaj superużytkownika.

```powershell
python manage.py createsuperuser
```

4. Uruchom serwer lokalny.

```powershell
python manage.py runserver
```

Aplikacja będzie dostępna pod `http://127.0.0.1:8000/`.

## Główne endpointy

- `/` - strona główna
- `/portfolio/` - projekty portfolio
- `/contact/` - formularz kontaktowy
- `/cv/` - widok CV
- `/admin/` - panel administracyjny
- `/i18n/` - endpointy internacjonalizacji Django

## Modele danych (aplikacja `pages`)

- `ContactMessage` - wiadomości z formularza kontaktowego
- `PortfolioProject` - projekty wyświetlane w portfolio
- `Person` - profil osoby do CV
- `CVSection` - sekcje CV (np. doświadczenie, umiejętności)
- `ExperienceItem` - pozycje doświadczenia

## Struktura projektu

```text
mysite/
|- manage.py
|- db.sqlite3
|- mysite/
|  |- settings.py.example
|  |- urls.py
|  `- ...
|- pages/
|  |- models.py
|  |- views.py
|  |- forms.py
|  |- admin.py
|  |- migrations/
|  `- templates/
`- static/
```

## Uwagi wdrożeniowe

- `.gitignore` jest przygotowany pod Django/Python.
- Domyślna konfiguracja używa `DEBUG=True` (tryb developerski).
- Przed wdrożeniem:
  - zmień nazwę `mysite/settings.py.example` na `mysite/settings.py` i dostosuj konfigurację do środowiska,
  - ustaw bezpieczny `SECRET_KEY`, ustaw `DEBUG=False` oraz skonfiguruj `ALLOWED_HOSTS`.

## References & Licenses

### Third-Party Software
* **Django**: Web framework used by this project. Source: [django](https://www.djangoproject.com/). License: [BSD 3-Clause](https://docs.djangoproject.com/en/6.0/faq/general/).
* **Bootstrap**: Frontend CSS/JS framework used for UI components and styling. Source: [Bootstrap](https://getbootstrap.com/). License: [MIT](https://getbootstrap.com/docs/5.0/about/license/).
* **jQuery**: JavaScript library used for DOM manipulation and client-side interactions. Source: [jQuery](https://jquery.com/). License: [MIT](https://jquery.com/license/).
* **Pillow**: Python imaging library used for image processing. Source: [Pillow](https://python-pillow.github.io/). License: [MIT-CMU / PIL Software License](https://pillow.readthedocs.io/en/stable/about.html).

### Licencja
Utworzony przeze mnie kod w tym repozytorium jest objęty licencją: **Apache 2.0 License**.