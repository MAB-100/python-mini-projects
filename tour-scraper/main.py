import sqlite3
import time

import requests
import selectorlib

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"}

conn = sqlite3.connect("data.db")
conn.execute("CREATE TABLE IF NOT EXISTS events (band TEXT, city TEXT, date TEXT)")


def scrape(url):
    """Download the page source."""
    response = requests.get(url, headers=HEADERS)
    return response.text


def extract(source):
    """Extract the tour text using the CSS selector in extract.yaml."""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    return extractor.extract(source)["tours"]


def parse(extracted):
    return [item.strip() for item in extracted.split(",")]


def read_from_db(row):
    band, city, date = row
    cursor = conn.execute("SELECT * FROM events WHERE band = ? AND city = ? AND date = ?",
                          (band, city, date))
    return cursor.fetchall()


def save_to_db(row):
    conn.execute("INSERT INTO events VALUES (?, ?, ?)", row)
    conn.commit()
    print("Saved to db:", row)


def send_email(row):
    print("New tour found:", row)


if __name__ == "__main__":
    while True:
        extracted = extract(scrape(URL))
        if extracted != "No upcoming tours":
            row = parse(extracted)
            if not read_from_db(row):
                save_to_db(row)
                send_email(row)
        time.sleep(2)
