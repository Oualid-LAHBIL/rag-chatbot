from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCS_DIR = Path("docs")

def load_and_split():
    documents = []
    for pdf in DOCS_DIR.glob("*.pdf"):
        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())
        print(f"Lu : {pdf.name}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = splitter.split_documents(documents)
    return chunks

if __name__ == "__main__":
    chunks = load_and_split()
    print(f"\n{len(chunks)} morceaux créés")
    print("\n--- Exemple de morceau ---")
    print(chunks[0].page_content)