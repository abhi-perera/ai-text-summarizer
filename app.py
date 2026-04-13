import streamlit as st
from ai_service import summarize_text

st.set_page_config(page_title="AI Text Summarizer")

st.title("AI Text Summarizer")

user_text = st.text_area("Paste your text here")

if st.button("Summarize"):
    if user_text.strip():
        result = summarize_text(user_text)
        st.subheader("Result")
        st.write(result)
    else:
        st.warning("Please enter some text.")