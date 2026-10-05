import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input(label="Your email address")
    user_message = st.text_area(label="Your message")
    button = st.form_submit_button(label="Send")

    if button:
        message = f"Subject: New message from {user_email}\n\nFrom: {user_email}\n{user_message}"
        send_email(message.encode("utf-8"))
        st.info("Your message was sent successfully")
