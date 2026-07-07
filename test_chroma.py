from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


print("Loading embeddings...")

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

print("Opening DB...")

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings,
    collection_name="supply_chain"
)

print("DB opened")

print("Collection Count:")
print(db._collection.count())