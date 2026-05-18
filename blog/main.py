from fastapi import FastAPI, HTTPException, Request, status, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.load_post import load_posts


app = FastAPI()

# Static folder
app.mount("/static", StaticFiles(directory="static"), name="static")


# Templates
template = Jinja2Templates(directory="templates")

# Load articles
articles : list[dict] = load_posts()

# HOME
@app.get("/", include_in_schema=False, name="home")
@app.get("/articles", include_in_schema=False, name="articles")
def home(request : Request):
    return template.TemplateResponse(request,"home.html", {"articles":articles})

# ADMIN
@app.get("/admin", include_in_schema=False, name="admin")
def admin(request : Request):
    return template.TemplateResponse(
        request,
        "dashbord.html",
        {
            "articles":articles
        }
        )

# ARTICLE PAGE
@app.get("/article/{article_id}", include_in_schema=False)
def article_page(request : Request, article_id:int):
    for article in articles:
        if article.get("id") == article_id:
            return template.TemplateResponse(
                request,
                "article.html",
                {"article": article},
                )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page not Found")

# Login
@app.get("/login", include_in_schema=False)
def login_page(request: Request):

    return template.TemplateResponse(
        request,
        "login.html",
        {
            "request": request
        }
    )

@app.post("/login")
def login(request: Request, username: str = Form(), password: str = Form()):

    if username == "admin" and password == "1234":
        return template.TemplateResponse(
            request,
            "dashbord.html",
            {
                "articles":articles
            }
            )

    raise HTTPException(
        status_code=401,
        detail="Identifiants incorrects"
    )

# API ROUTES

@app.get("/api/articles")
def get_articles():
    return articles

@app.get("/api/articles/{article_id}")
def get_article(article_id: int):
    for article in articles:
        if article.get("id") == article_id:
            return article
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page not Found")

print(articles)