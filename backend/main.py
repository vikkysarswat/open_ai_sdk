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

@app.get("/mcp/manifest")
def manifest():
    """MCP manifest so ChatGPT connector knows about available tools."""
    return {
        "name": "news_mcp_server",
        "version": "1.0.0",
        "description": "Fetches latest news articles for ChatGPT PlayCards.",
        "tools": [
            {
                "name": "news",
                "description": "Get top headlines using News API.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "country": {"type": "string", "default": "in"},
                        "limit": {"type": "integer", "default": 5}
                    },
                    "required": []
                },
                "output_schema": {"type": "array", "items": {"type": "object"}}
            }
        ]
    }

@app.get("/tools/news", response_model=List[Dict])
def get_news(country: str = "in", limit: int = 5):
    """Return a list of news articles."""
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"
    resp = requests.get(url)
    data = resp.json()

    articles = data.get("articles", [])
    cards = []
    for art in articles[:limit]:
        cards.append({
            "title": art.get("title"),
            "description": art.get("description", ""),
            "image": art.get("urlToImage"),
            "url": art.get("url"),
            "publishedAt": art.get("publishedAt", "")[:10],
            "source": art.get("source", {}).get("name", "")
        })
    return cards
