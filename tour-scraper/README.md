# Tour Scraper

Polls a web page for upcoming tour dates. It extracts the tour text with a CSS selector defined in `extract.yaml` (selectorlib), stores each new tour in SQLite, and sends a notification only for tours it hasn't seen before.

## Run

```bash
pip install -r requirements.txt
python main.py
```
