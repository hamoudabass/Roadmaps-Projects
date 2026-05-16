import os
import json

directory = "articles/"

def next_number():
    fichiers = [f for f in os.listdir(directory) if f.endswith(".json")]
    return len(fichiers) + 1

def add_article(answer: dict):
    number = next_number()
    fichier = f"articles/{number}.json"

    with open(fichier, "w") as f:
        json.dump(answer, f, indent=4, ensure_ascii=False)

    return {
        'status': '200',
        'article': fichier
    }

print(add_article({"id": 1,
    "title": "Mon premier article",
    "content": "Le contenu de l'article...",
    "published_at": "Vendredi 15 Mai 2026",
    "slug": "mon-premier-article"}))