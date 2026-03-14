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

## Virtual Environment (venv)

Create and activate a local virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Quick Start (Local)

1. Install dependencies.

```powershell
pip install -r requirements.txt
```

2. Run migrations.

```powershell
python manage.py migrate
```

3. (Optional) Create an admin user.

```powershell
python manage.py createsuperuser
```

4. Start the development server.

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

## References & Licenses

### Third-Party Software
* **Django**: Web framework used by this project. Source: [django](https://www.djangoproject.com/). License: [BSD 3-Clause](https://docs.djangoproject.com/en/6.0/faq/general/).
* **Bootstrap**: Frontend CSS/JS framework used for UI components and styling. Source: [Bootstrap](https://getbootstrap.com/). License: [MIT](https://getbootstrap.com/docs/5.0/about/license/).
* **jQuery**: JavaScript library used for DOM manipulation and client-side interactions. Source: [jQuery](https://jquery.com/). License: [MIT](https://jquery.com/license/).
* **Pillow**: Python imaging library used for image processing. Source: [Pillow](https://python-pillow.github.io/). License: [MIT-CMU / PIL Software License](https://pillow.readthedocs.io/en/stable/about.html).

### License
My original code in this repository is licensed under the **Apache 2.0 License**.