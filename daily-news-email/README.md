# Daily News Email

Fetches the 20 most recent English-language articles on a topic from [NewsAPI](https://newsapi.org) and emails the headlines, descriptions and links to you as a digest. Run it on a schedule (cron or Task Scheduler) to get a daily email.

## Run

```bash
pip install -r requirements.txt
export NEWS_API_KEY=your-newsapi-key
export EMAIL_ADDRESS=you@gmail.com
export EMAIL_APP_PASSWORD=your-gmail-app-password
python main.py
```

Change `topic` in `main.py` to follow a different subject.
