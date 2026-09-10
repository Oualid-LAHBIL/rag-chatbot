from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")


def repondre(question):
    docs = db.similarity_search(question, k=4)
    contexte = "\n\n".join(d.page_content for d in docs)
    prompt = f"""Tu es un assistant qui répond uniquement à partir du contexte ci-dessous.
Si la réponse n'est pas dans le contexte, dis que tu ne sais pas.

Contexte :
{contexte}

Question : {question}

Réponse :"""
    reponse = llm.invoke(prompt)
    return reponse.text, docs


if __name__ == "__main__":
    while True:
        question = input("\nTa question (tape q pour quitter) : ")
        if question.strip().lower() == "q":
            break
        texte, docs = repondre(question)
        print("\n" + texte)
        pages = sorted({d.metadata.get("page", 0) + 1 for d in docs})
        print(f"\nSources : pages {pages}")