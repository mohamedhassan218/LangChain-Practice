from transformers import pipeline
import streamlit as st
import textwrap

st.title("Text Summarizer")

with st.sidebar:
    with st.form(key="my_form"):
        full_text = st.sidebar.text_area(
            label="Enter your text", max_chars=350
        )
        submit_button = st.form_submit_button(label="Submit")

if st.form_submit_button('Submit'):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    response = summarizer(full_text, max_length=150, min_length=40, do_sample=False)
    st.subheader("Answer:")
    st.text(textwrap.fill(response[0]['summary_text'], width=70))