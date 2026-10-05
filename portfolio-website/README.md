# Portfolio Website

A two-page Streamlit portfolio site:

- **Home:** a short bio, plus a two-column list of the projects in this repository loaded from `data.csv`
- **Contact Me:** a form that emails the visitor's message to the site owner over Gmail SMTP

## Run

```bash
pip install -r requirements.txt
export EMAIL_ADDRESS=you@gmail.com
export EMAIL_APP_PASSWORD=your-gmail-app-password   # a Gmail App Password, not your normal password
streamlit run home.py
```
