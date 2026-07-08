import ollama

from app.rag import retrieve_context

from app.tools import (
    get_delivery_context,
    get_inventory_context,
    get_supplier_context,
    get_sales_context
)

LLM_MODEL = "qwen2.5:3b"


def choose_tool(question):

    q = question.lower()

    # ---------- RAG QUESTIONS ----------
    if any(word in q for word in [
        "policy",
        "procedure",
        "guideline",
        "management",
        "process",
        "responsibility",
        "document",
        "reorder",
        "sop"
    ]):
        return "rag"

    # ---------- DELIVERY ----------
    if any(word in q for word in [
        "delivery",
        "delayed",
        "delay",
        "shipment"
    ]):
        return "delivery"

    # ---------- INVENTORY ----------
    if any(word in q for word in [
        "inventory",
        "stock",
        "quantity"
    ]):
        return "inventory"

    # ---------- SUPPLIER ----------
    if any(word in q for word in [
        "supplier",
        "vendor",
        "rating"
    ]):
        return "supplier"

    # ---------- SALES ----------
    if any(word in q for word in [
        "sales",
        "revenue",
        "order"
    ]):
        return "sales"

    # ---------- DEFAULT ----------
    return "rag"


def generate_answer(question, context):

    prompt = f"""
You are a Supply Chain AI Assistant.

Answer ONLY from the given context.

If the answer is not present in the context, reply exactly:

"I couldn't find that information."

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def run_agent(question):

    print("=" * 60)
    print("Question:", question)

    tool = choose_tool(question)

    print("Tool Selected:", tool)

    if tool == "delivery":
        context = get_delivery_context()

    elif tool == "inventory":
        context = get_inventory_context()

    elif tool == "supplier":
        context = get_supplier_context()

    elif tool == "sales":
        context = get_sales_context()

    else:
        context = retrieve_context(question)

    print("\nContext:")
    print(context[:500])

    answer = generate_answer(
        question,
        context
    )

    print("\nAnswer:")
    print(answer)

    print("=" * 60)

    return answer