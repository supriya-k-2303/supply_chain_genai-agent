from app.rag import retrieve_context

print("Before retrieve_context")

context = retrieve_context("What is supply chain?")

print("After retrieve_context")
print(context)