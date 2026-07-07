```markdown
# 🚚 Supply Chain GenAI Assistant

An AI-powered Supply Chain Assistant that combines **Retrieval Augmented Generation (RAG)**, **structured data analytics**, and **LLM-based reasoning** to answer business questions from supply chain documents and operational datasets.

The system can answer questions related to:
- Supply chain policies
- Inventory management
- Supplier performance
- Delivery analysis
- Sales insights
- Operational metrics


## 🏗️ Architecture

```

User
|
|
Streamlit UI
|
|
FastAPI Backend
|
|
AI Agent Router
|
+---------------------+
|                     |
|                     |
RAG Pipeline       Data Analytics Tool
|                     |
ChromaDB              CSV Dataset
|                     |
Supply Chain PDFs     Pandas
|
|
Ollama LLM
|
|
Generated Answer

```


# ✨ Features

## 1. Retrieval Augmented Generation (RAG)

- Loads supply chain PDF documents
- Creates embeddings
- Stores vectors in ChromaDB
- Retrieves relevant information based on user questions
- Generates context-aware answers using LLM


Example:

**Question:**
```

What is reorder policy?

```

**Answer:**
```

When inventory falls below 100 units,
the warehouse system automatically creates a reorder request.

```


---

## 2. Supply Chain Data Analytics

Uses `supply_chain_enriched.csv` containing operational data.

The assistant can answer:

- How many deliveries were delayed?
- What is average supplier rating?
- What is total sales?
- What inventory information is available?


Example:

```

Question:
How many deliveries were delayed?

Answer:
737 deliveries were delayed.

```


---

## 3. AI Agent Routing

The system automatically decides whether a question requires:

- Document retrieval (RAG)
- Structured data analysis


Example:

```

"What is inventory policy?"
|
v
RAG

"How many deliveries were delayed?"
|
v
Data Analytics Tool

```


---

# 🛠️ Technology Stack

## Programming Language

- Python 3.11


## Large Language Model

- Ollama
- Qwen2.5:3B


## Generative AI Framework

- LangChain components
- Custom AI Agent Router


## Retrieval Augmented Generation

- Sentence Transformers
- ChromaDB Vector Database


## Embedding Model

- all-MiniLM-L6-v2


## Backend API

- FastAPI
- Uvicorn


## Frontend

- Streamlit


## Data Processing

- Pandas
- CSV Analytics


## Database / Storage

- ChromaDB (Vector Database)
- Local CSV Dataset


---

# 📂 Project Structure

```

final_agent/

│
├── app/
│   |
│   ├── api.py              # FastAPI backend
│   ├── ui.py               # Streamlit interface
│   ├── graph.py            # Agent routing logic
│   ├── rag.py              # RAG pipeline
│   ├── tools.py            # Data analytics tools
│
├── data/
│   |
│   ├── supply_chain_enriched.csv
│   |
│   └── pdf/
│       ├── inventory_policy.pdf
│       ├── supplier_policy.pdf
│       └── other documents
│
├── chroma_db/              # Vector database
│
├── ingest.py               # Document ingestion
├── requirements.txt
└── README.md

````


# ⚙️ Installation

Clone repository:

```bash
git clone <repository-url>

cd final_agent
````

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

# 🚀 Running the Application

## Start FastAPI Backend

```bash
python -m uvicorn app.api:app --reload
```

API available:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

## Start Streamlit UI

Open another terminal:

```bash
streamlit run app/ui.py
```

UI available:

```
http://localhost:8501
```

# 💡 Example Questions

## RAG Questions

```
What is supply chain management?

What is reorder policy?

Explain supplier evaluation process.

What are warehouse responsibilities?
```

## Data Analytics Questions

```
How many deliveries were delayed?

What is average supplier rating?

What is total sales?

What inventory information is available?
```

# 🎯 Skills Demonstrated

* Generative AI Application Development
* Retrieval Augmented Generation (RAG)
* Vector Databases
* Embeddings
* LLM Integration
* AI Agent Design
* Supply Chain Analytics
* REST API Development
* Data Processing
* End-to-End AI Application Deployment

# 🔮 Future Improvements

* Replace rule-based routing with LLM tool calling
* Add LangGraph state workflow
* Add conversation memory
* Add ML model for delivery delay prediction
* Add Docker deployment
* Add monitoring and logging


Built as an end-to-end Generative AI + Data Science portfolio project.



