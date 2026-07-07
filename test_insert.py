from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document


print("Loading embedding model")

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

docs = [
    Document(
        page_content="Supply chain manages movement of goods from supplier to customer."
    )
]

print("Creating Chroma")

db = Chroma(
    persist_directory="test_chroma",
    collection_name="test_collection",
    embedding_function=embeddings
)

print("Adding document")

ids = db.add_documents(docs)

print("Inserted:", ids)

print("Count:", db._collection.count())