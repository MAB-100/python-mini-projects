import streamlit as st
import pandas as pd

REPO_URL = "https://github.com/MAB-100/python-mini-projects/tree/main"

st.set_page_config(page_title="Abbas Bukhari - Portfolio", page_icon=":computer:",
                   layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Muhammad Abbas Bukhari")
    st.write("AI Engineer. This site lists the small Python projects in this repository, "
             "from data analysis and machine learning to web and desktop apps.")

df = pd.read_csv("data.csv", sep=";")
half = (len(df) + 1) // 2

col3, empty_col, col4 = st.columns([2, 0.5, 2])

with col3:
    for index, row in df[:half].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.write(f"[Source Code]({REPO_URL}/{row['folder']})")

with col4:
    for index, row in df[half:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.write(f"[Source Code]({REPO_URL}/{row['folder']})")
