# app/main.py
from fastapi import FastAPI
import httpx

app = FastAPI(title="Mini News Collector")

# Basit bir memory cache
ARTICLES = []

NEWS_API = "https://hn.algolia.com/api/v1/search?query=devops"  # örnek: HackerNews API

@app.get("/")
def root():
    return {"message": "Mini News Collector is running!"}

@app.get("/articles")
def list_articles():
    return {"articles": ARTICLES}

@app.post("/refresh")
def refresh_articles():
    global ARTICLES
    try:
        resp = httpx.get(NEWS_API, timeout=10.0)
        resp.raise_for_status()
        data = resp.json()
        ARTICLES = [
            {"title": hit["title"], "url": hit["url"]}
            for hit in data.get("hits", [])[:5]  # ilk 5 haber
            if hit.get("title") and hit.get("url")
        ]
        return {"count": len(ARTICLES), "articles": ARTICLES}
    except Exception as e:
        return {"error": str(e)}