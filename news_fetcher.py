import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

api_key = os.getenv("NEWS_API_KEY")




def get_stock_news(ticker):
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&language=en&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if data.get("status") != "ok":
        return []

    articles = data.get("articles", [])[:5]  # return top 5 articles
    return [{
        "title": article["title"],
        "url": article["url"],
        "source": article["source"]["name"],
        "publishedAt": article["publishedAt"]
    } for article in articles]
