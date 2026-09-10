\# Chatbot RAG sur un cours de NLP



Chatbot qui répond aux questions à partir d'un PDF de cours, en citant les pages sources.



\## Fonctionnement

1\. Lecture et découpage du PDF en morceaux (LangChain)

2\. Embeddings multilingues (sentence-transformers) stockés dans Chroma

3\. Recherche des 8 passages les plus proches de la question

4\. Génération de la réponse par Gemini, uniquement à partir de ces passages



\## Technologies

Python, LangChain, ChromaDB, sentence-transformers, Gemini API, Streamlit



\## Lancer le projet

pip install -r requirements.txt

python index.py

streamlit run app.py

(définir la variable d'environnement GOOGLE\_API\_KEY avant)

