import streamlit as st

# Read HTML file
with open("tt.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render HTML
st.components.v1.html(html_content, height=600, scrolling=True)
