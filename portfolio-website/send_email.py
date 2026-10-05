import os
import smtplib
import ssl


def send_email(message):
    """Send a message to the site owner's inbox through Gmail SMTP."""
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_APP_PASSWORD")
    if not username or not password:
        raise RuntimeError("Set EMAIL_ADDRESS and EMAIL_APP_PASSWORD (see .env.example)")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)
