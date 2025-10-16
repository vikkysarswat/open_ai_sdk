from fastapi import FastAPI
from typing import List, Dict
import requests
from datetime import datetime
import os

app = FastAPI(title="News MCP Server")

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "your_default_key")

@app.get("/")
def home():
    return {"status": "✅ News MCP server running"}

@app.get("/tools/news", response_model=List[Dict])
def get_news():
    """Return a list of news articles"""
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    resp = requests.get(url)
    data = resp.json()

    articles = data.get("articles", [])
    cards = []
    for art in articles[:6]:
        cards.append({
            "title": art["title"],
            "description": art.get("description", ""),
            "image": art.get("urlToImage"),
            "url": art["url"],
            "publishedAt": art.get("publishedAt", "")[:10],
            "source": art.get("source", {}).get("name", "")
        })
    return cards
