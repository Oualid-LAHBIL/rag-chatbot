import streamlit as st
from chat import repondre

st.set_page_config(page_title="Chatbot RAG - Cours NLP", page_icon="📚")
st.title("📚 Chatbot RAG sur mon cours de NLP")
st.caption("Pose une question, la réponse vient uniquement de mon PDF.")

question = st.text_input("Ta question :")

if question:
    with st.spinner("Recherche en cours..."):
        texte, docs = repondre(question)
    st.write(texte)
    pages = sorted({d.metadata.get("page", 0) + 1 for d in docs})
    st.caption(f"Sources : pages {pages}")