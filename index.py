from ingest import load_and_split
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

chunks = load_and_split()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="chroma_db",
)

print(f"\n{len(chunks)} morceaux indexés dans chroma_db")