import os
import requests
from send_email import send_email

topic = "tesla"
api_key = os.getenv("NEWS_API_KEY")
if not api_key:
    raise RuntimeError("Set NEWS_API_KEY (get a free key at https://newsapi.org)")

url = "https://newsapi.org/v2/everything"
params = {"q": topic, "sortBy": "publishedAt", "language": "en", "apiKey": api_key}

response = requests.get(url, params=params)
content = response.json()

body = "Subject: Today's news\n\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += f"{article['title']}\n{article['description']}\n{article['url']}\n\n"

send_email(message=body.encode("utf-8"))
