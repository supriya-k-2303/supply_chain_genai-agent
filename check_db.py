from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings,
    collection_name="supply_chain"
)

print("Total documents:", vectorstore._collection.count())

docs = vectorstore.similarity_search("", k=20)

for i, doc in enumerate(docs, 1):
    print(f"\n----- Document {i} -----")
    print(doc.page_content[:500])