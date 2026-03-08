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

## Szybki start (lokalnie)

1. Utw�rz i aktywuj środowisko wirtualne.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Zainstaluj zależności.

```powershell
pip install "Django>=6,<7" Pillow
```

3. Wykonaj migracje.

```powershell
python manage.py migrate
```

4. (Opcjonalnie) utwórz konto administratora.

```powershell
python manage.py createsuperuser
```

5. Uruchom serwer developerski.

```powershell
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem `http://127.0.0.1:8000/`.

## G��wne endpointy

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

## Uwagi wdro�eniowe

- `.gitignore` jest przygotowany pod Django/Python.
- Domyślna konfiguracja używa `DEBUG=True` (tryb developerski).
- Przed wdrożeniem:
  - zmień nazwę `mysite/settings.py.example` na `mysite/settings.py` i dostosuj konfigurację do środowiska,
  - ustaw bezpieczny `SECRET_KEY`, ustaw `DEBUG=False` oraz skonfiguruj `ALLOWED_HOSTS`.
