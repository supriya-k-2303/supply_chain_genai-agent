from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os

PDF_FOLDER = "data/pdf"
CHROMA_PATH = "chroma_db"

print("Folder Exists :", os.path.exists(PDF_FOLDER))
print("Files :", os.listdir(PDF_FOLDER))

loader = PyPDFDirectoryLoader(PDF_FOLDER)

documents = loader.load()

print(f"Loaded {len(documents)} pages.")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks.")

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# vectorstore = Chroma.from_documents(
#     documents=chunks,
#     embedding=embeddings,
#     persist_directory=chroma_db,
#     collection_name="supply_chain"
# )

# print("\n====================================")
# print("Vector Database Created Successfully")
# print(f"Chunks : {len(chunks)}")
# print("====================================")



# print("Created", len(chunks), "chunks")

# print("Number of chunks going into Chroma:", len(chunks))


# vectorstore = Chroma.from_documents(
#     documents=chunks,
#     embedding=embeddings,
#     persist_directory="chroma_db",
#     collection_name="supply_chain"
# )

# print("Chroma DB created successfully")


# from langchain_chroma import Chroma

# vectorstore = Chroma.from_documents(
#     documents=chunks,
#     embedding=embeddings,
#     persist_directory="chroma_db",
#     collection_name="supply_chain"
# )

# print("Documents inserted:", vectorstore._collection.count())


print("Starting Chroma insertion...")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db",
    collection_name="supply_chain"
)

print("Chroma insertion finished")

print("Documents inserted:", vectorstore._collection.count())