from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

print("Loading embeddings...")

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

print("Connecting to Chroma...")

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings,
    collection_name="supply_chain"
)

print("Retriever ready.")


def retrieve_context(question: str):

    docs = vectorstore.similarity_search(
        question,
        k=5
    )

    if not docs:
        return "No relevant context found."

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )