import json
import os

directory = "articles/"

def load_posts():
    
    articles : list = []
    fichiers = os.listdir("articles")
    for fichier in fichiers:
        article_path = (directory + fichier)
        with open(article_path) as f:
            data = json.load(f)
        articles.append(data)
    return articles
