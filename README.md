# Python Mini Projects

18 small, self-contained Python projects covering data analysis and machine learning, web APIs and web apps, desktop GUIs, and automation scripts.

I built them in 2024 while working through *The Python Mega Course* by Ardit Sulce, then collected them into one repository and cleaned them up: secrets moved to environment variables, bugs fixed, and a README added for each project.

## Projects

### Data & Machine Learning

| Project | Description | Tech |
|---|---|---|
| [movie-recommender](movie-recommender) | Three recommenders: popularity-based (IMDB weighted rating), content-based (TF-IDF + cosine similarity) and collaborative filtering (SVD) | pandas, scikit-learn, Surprise |
| [book-text-analysis](book-text-analysis) | Word-frequency statistics and chapter-by-chapter sentiment analysis of a book | regex, NLTK, VADER |
| [webcam-motion-detector](webcam-motion-detector) | Detects objects entering the webcam view and saves a snapshot | OpenCV |

### Web APIs & Web Apps

| Project | Description | Tech |
|---|---|---|
| [weather-data-api](weather-data-api) | REST API serving historical temperatures by station, by date and by year | Flask, pandas |
| [weather-forecast-dashboard](weather-forecast-dashboard) | Interactive five-day forecast with temperature chart and sky icons | Streamlit, Plotly, OpenWeather API |
| [portfolio-website](portfolio-website) | Multi-page portfolio site with a working contact form | Streamlit, SMTP |
| [job-application-flask](job-application-flask) | Job application form that saves submissions to a database | Flask, SQLAlchemy, Bootstrap |
| [job-application-django](job-application-django) | The same form in Django, with an admin panel to review submissions | Django, Bootstrap |
| [restaurant-menu-django](restaurant-menu-django) | Restaurant menu showing which dishes are available, managed through the admin panel | Django class-based views |

### Desktop Apps

| Project | Description | Tech |
|---|---|---|
| [todo-app](todo-app) | One todo list with three front ends: CLI, desktop GUI and web app | FreeSimpleGUI, Streamlit |
| [student-management-sqlite](student-management-sqlite) | Student records app with add, edit and delete | PyQt6, SQLite |
| [student-management-mysql](student-management-mysql) | The same app backed by MySQL, with search | PyQt6, MySQL |

### Automation & Scripting

| Project | Description | Tech |
|---|---|---|
| [daily-news-email](daily-news-email) | Fetches the latest articles on a topic and emails a digest | NewsAPI, smtplib |
| [tour-scraper](tour-scraper) | Watches a web page for new tour dates and stores new ones in a database | requests, selectorlib, SQLite |
| [excel-to-pdf-invoices](excel-to-pdf-invoices) | Turns Excel invoice files into formatted PDF invoices | pandas, FPDF |
| [invoice-generator-package](invoice-generator-package) | The invoice generator packaged as a pip-installable library | setuptools |
| [pdf-template-generator](pdf-template-generator) | Generates a lined notebook PDF with one section per topic from a CSV | FPDF, pandas |
| [hotel-booking-oop](hotel-booking-oop) | Hotel booking flow modelled with classes and inheritance | OOP, pandas |

## Running a project

Each project has its own `requirements.txt` and README. For example:

```bash
cd weather-forecast-dashboard
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Projects that use an API key or email login read it from environment variables. [`.env.example`](.env.example) lists them all.

## License

[MIT](LICENSE)
