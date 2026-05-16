from fastapi import FastAPI, HTTPException, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.load_post import load_posts


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

template = Jinja2Templates(directory="templates")

articles : list[dict] = load_posts()

@app.get("/", include_in_schema=False, name="home")
@app.get("/articles", include_in_schema=False, name="articles")
def home(request : Request):
    return template.TemplateResponse(request,"home.html", {"articles":articles})

@app.get("/admin", include_in_schema=False, name="admin")
def admin(request : Request):
    return template.TemplateResponse(request,"dashbord.html", {"articles":articles})



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

print(articles)