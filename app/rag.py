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

    print("Creating retriever...")

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    print("Retriever created")

    docs = vectorstore.similarity_search(question, k=3)

    print("Similarity search completed")

    if len(docs) == 0:
        return "No documents found."

    return "\n\n".join(doc.page_content for doc in docs)


# def retrieve_context(question: str):

#     print("Generating query embedding...")

#     retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

#     print("Calling retriever...")

#     docs = retriever.invoke(question)

#     print("Retriever finished.")

#     if not docs:
#         return "No relevant information found."

#     return "\n\n".join(doc.page_content for doc in docs)