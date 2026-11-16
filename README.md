# FastAPI SSR Personal Portfolio

A server-side rendered, single-page portfolio for **Akash Bondada**, built with FastAPI and Jinja2. All portfolio sections are rendered by `GET /`; navigation uses same-page anchor links.

## Features

- FastAPI + Uvicorn local application
- Jinja2 template inheritance with `base.html` and `index.html`
- Static CSS and profile image served through `StaticFiles`
- Persistent light/dark mode using an HTTP-only `theme` cookie
- Responsive, accessible portfolio layout with About, Skills, Projects, Education and Contact sections

## Stack

Python 3.10+, FastAPI, Uvicorn, Jinja2, HTML5 and CSS3.

## Structure

```text
portfolio_app/
├── main.py
├── requirements.txt
├── static/css/style.css
├── static/images/profile.jpg
├── templates/base.html
├── templates/index.html
├── README.md
└── .gitignore
```

## Run on Windows PowerShell

```powershell
cd portfolio_app
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn main:app --reload
```

Open <http://127.0.0.1:8000/>. The theme form posts to `/set-theme`; the backend toggles the `theme` cookie with a 30-day lifetime, `HttpOnly`, `SameSite=Lax`, and a 303 redirect. No JavaScript or localStorage is used.

## Testing checklist

With the server running, verify `GET /`, `/static/css/style.css`, `/static/images/profile.jpg`, both theme transitions, the 303 response and cookie attributes. Use browser Application/Storage → Cookies to confirm `theme=dark` or `theme=light` remains after refresh.

## Submission notes

The contact section presents four icon rows that link directly to the supplied email address, phone number, GitHub and LinkedIn profiles. Only the email address is printed as visible text; the phone number and profile URLs stay in the link targets. The profile image is a supplied local asset and can be replaced at `static/images/profile.jpg`.

**Author:** Akash Bondada  
**Repository name:** `fastapi-ssr-personal-portfolio`
