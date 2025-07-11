import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env



API_KEY = os.getenv("NEWS_API_KEY")  # Store this safely!

def get_stock_news(ticker, max_results=5):
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&q={ticker}&language=en&category=business"
    response = requests.get(url)
    data = response.json()

    if "results" not in data:
        return []

    articles = data["results"][:max_results]
    return [{
        "title": article.get("title"),
        "url": article.get("link"),
        "source": article.get("source_id"),
        "publishedAt": article.get("pubDate", "")[:10],
        "description": article.get("description"),
        "image": article.get("image_url")
    } for article in articles]



