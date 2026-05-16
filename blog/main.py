from fastapi import FastAPI, HTTPException, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja1Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

template = Jinja2Templates(directory="templates")

articles : list[dict] = [
    {
        "id": 1,
        "title": "Mon premier article",
        "content": "Le contenu de l'article...",
        "published_at": "2026-05-12",
        "slug": "mon-premier-article"
    },
    {
        "id": 2,
        "title": "Mon deuxième article",
        "content": "Le contenu de l'article...",
        "published_at": "2026-05-12",
        "slug": "mon-deuxième-article"
    },
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/articles", include_in_schema=False, name="articles")
def home(request : Request):
    return template.TemplateResponse(request,"home.html", {"articles":articles})

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


@app.get("/api/articles")
def get_articles():
    return articles

@app.get("/api/articles/{article_id}")
def get_article(article_id: int):
    for article in articles:
        if article.get("id") == article_id:
            return article
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Page not Found")

