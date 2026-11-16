from datetime import datetime
from urllib.parse import urlparse

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(title="Akash Bondada | Python Full Stack Developer")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.middleware("http")
async def prevent_stale_html(request: Request, call_next):
    """Serve HTML fresh so a redesigned page is never shown from browser cache."""
    response = await call_next(request)
    if response.headers.get("content-type", "").startswith("text/html"):
        response.headers["Cache-Control"] = "no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
    return response

SKILLS = [
    {"group": "Python & Backend", "icon": "01", "items": ["Python", "FastAPI", "Flask", "REST API Development"]},
    {"group": "Java Backend", "icon": "02", "items": ["Java", "Spring Boot", "Hibernate"]},
    {"group": "Frontend", "icon": "03", "items": ["HTML5", "CSS3", "Bootstrap", "JavaScript", "Thymeleaf"]},
    {"group": "Data & Tools", "icon": "04", "items": ["MySQL", "Oracle SQL", "Git", "GitHub", "VS Code", "PyCharm", "Postman", "Docker"]},
]

PROJECTS = [
    {
        "number": "01",
        "title": "Task Manager Application",
        "description": "A Python-based task management application built around FastAPI, with a clean HTML, CSS and JavaScript interface for organizing tasks.",
        "technologies": ["Python", "FastAPI", "HTML", "CSS", "JavaScript"],
        "featured": True,
        "focus": "Python focus",
    },
    {
        "number": "02",
        "title": "Hand Gesture Recognition",
        "description": "A computer-vision project combining hand gesture recognition with voice commands using a Python machine-learning stack.",
        "technologies": ["Python", "Computer Vision", "TensorFlow", "OpenCV", "MediaPipe", "Speech Recognition"],
        "featured": False,
        "focus": "ML focus",
    },
    {
        "number": "03",
        "title": "Student Management System",
        "description": "A Java web application for student record CRUD operations, built with Spring Boot, Thymeleaf and MySQL.",
        "technologies": ["Java", "Spring Boot", "Thymeleaf", "MySQL", "CRUD"],
        "featured": False,
        "focus": "Java focus",
    },
]

EDUCATION = [
    {"degree": "MCA", "institution": "Dr. Lankapalli Bullayya PG College", "university": "Andhra University", "year": "2024"},
    {"degree": "B.Sc (MPCS)", "institution": "Aditya Degree College", "university": "Andhra University", "year": "2022"},
]


def get_theme(request: Request) -> str:
    theme = request.cookies.get("theme", "light")
    return theme if theme in {"light", "dark"} else "light"


def safe_redirect_target(referer: str | None) -> str:
    """Allow only local absolute referrers, preventing open redirects."""
    if not referer:
        return "/"
    parsed = urlparse(referer)
    if parsed.scheme not in {"http", "https"} or parsed.hostname not in {"localhost", "127.0.0.1", "::1"}:
        return "/"
    return parsed.path or "/"


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "theme": get_theme(request),
            "projects": PROJECTS,
            "skills": SKILLS,
            "education": EDUCATION,
            "name": "Akash Bondada",
            "title": "Python Full Stack Developer | MCA Graduate",
            "year": datetime.now().year,
        },
    )


@app.post("/set-theme")
async def set_theme(request: Request):
    current_theme = request.cookies.get("theme", "light")
    new_theme = "dark" if current_theme == "light" else "light"
    response = RedirectResponse(url=safe_redirect_target(request.headers.get("referer")), status_code=303)
    response.set_cookie(
        key="theme",
        value=new_theme,
        max_age=2592000,
        httponly=True,
        samesite="lax",
        path="/",
        secure=False,
    )
    return response
