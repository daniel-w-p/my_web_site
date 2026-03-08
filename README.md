# ITechMind - portfolio site (Django)

Simple portfolio/CV website with a contact form, built with Django.

Polish version: `README_PL.md`.

## Features

- Home page (`/`)
- Portfolio page (`/portfolio/`)
- Contact form that stores messages in the database (`/contact/`)
- CV page driven by database models (`/cv/`)
- Django admin panel (`/admin/`)
- Initial i18n setup (PL/EN)

## Tech Stack

- Python 3.12+
- Django 6.x
- SQLite (default local database)

## Quick Start (Local)

1. Create and activate a virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies.

```powershell
pip install "Django>=6,<7" Pillow
```

3. Run migrations.

```powershell
python manage.py migrate
```

4. (Optional) Create an admin user.

```powershell
python manage.py createsuperuser
```

5. Start the development server.

```powershell
python manage.py runserver
```

The app will be available at `http://127.0.0.1:8000/`.

## Main Endpoints

- `/` - home page
- `/portfolio/` - portfolio projects
- `/contact/` - contact form
- `/cv/` - CV page
- `/admin/` - admin panel
- `/i18n/` - Django i18n endpoints

## Data Models (`pages` app)

- `ContactMessage` - messages from the contact form
- `PortfolioProject` - projects displayed in portfolio
- `Person` - person profile for CV
- `CVSection` - CV sections (e.g. experience, skills)
- `ExperienceItem` - experience entries

## Project Structure

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

## Deployment Notes

- `.gitignore` is prepared for Django/Python.
- Default setup uses `DEBUG=True` (development mode).
- Before deployment:
  - rename `mysite/settings.py.example` to `mysite/settings.py` and adjust it to your environment,
  - set a secure `SECRET_KEY`, set `DEBUG=False`, and configure `ALLOWED_HOSTS`.
