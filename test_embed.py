from langchain_ollama import OllamaEmbeddings

emb = OllamaEmbeddings(model="nomic-embed-text")

print("Before")

x = emb.embed_query("hello world")

print("After")

print(len(x))