from app.graph import run_agent


print("🚚 Supply Chain AI Agent")
print("Type 'exit' to stop\n")


while True:

    question = input("Ask: ")

    if question.lower() == "exit":
        break

    answer = run_agent(question)

    print("\nAnswer:")
    print(answer)
    print("\n" + "-" * 50)