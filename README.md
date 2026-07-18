# RAG Technical Documentation Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about technical documentation. The system ingests documentation from websites, converts it into vector embeddings, stores it in ChromaDB, and retrieves relevant context to generate accurate answers using Google's Gemini model.

---

## Features

- Website documentation ingestion
- PDF and Markdown document support
- Semantic search using ChromaDB
- Retrieval-Augmented Generation (RAG)
- LangGraph workflow orchestration
- Google Gemini integration
- FastAPI REST API
- Streamlit chat interface
- Source citation for every answer
- Swagger API documentation

---

# Project Architecture

```
                    +--------------------+
                    |    Streamlit UI    |
                    +---------+----------+
                              |
                              v
                    +--------------------+
                    |     FastAPI API    |
                    +---------+----------+
                              |
               +--------------+--------------+
               |                             |
               v                             v
      Document Ingestion              User Question
               |                             |
               v                             |
      Load & Split Documents                 |
               |                             |
               v                             |
     HuggingFace Embeddings                  |
               |                             |
               v                             |
           ChromaDB <-------------------------+
               |
               v
          Retriever
               |
               v
           LangGraph
      (Retrieve → Generate)
               |
               v
       Google Gemini 2.5 Flash
               |
               v
            Response
```

---

# Tech Stack

- Python
- FastAPI
- Streamlit
- LangGraph
- LangChain
- Google Gemini 2.5 Flash
- ChromaDB
- HuggingFace Embeddings
- BeautifulSoup
- PyPDF

---

# Project Structure

```
RAG/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── graph/
│   ├── ingestion/
│   └── services/
│
├── frontend/
│
├── documents/
├── database/
├── scripts/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Setup

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-documentation-assistant.git

cd rag-documentation-assistant
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_API_KEY

LLM_MODEL=gemini-2.5-flash

LLM_TEMPERATURE=0

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

CHROMA_DB=database/chroma

COLLECTION_NAME=technical_docs

TOP_K=5
```

---

# Running the Application

## Backend

```bash
uvicorn main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Frontend

```bash
streamlit run frontend/app.py
```

---

# API Endpoints

## Health Check

```
GET /health
```

Example Response

```json
{
  "status": "healthy"
}
```

---

## Ingest Documentation

```
POST /ingest
```

Example Request

```json
{
  "source_type": "website",
  "source": "https://fastapi.tiangolo.com/"
}
```

Example Response

```json
{
  "message": "Documents ingested successfully"
}
```

---

## Chat

```
POST /chat
```

Example Request

```json
{
  "question": "How do I install FastAPI?"
}
```

Example Response

```json
{
  "answer": "Install FastAPI using pip.",
  "sources": [
    "https://fastapi.tiangolo.com/"
  ]
}
```

---

# Document Corpus

The project currently supports:

- Technical websites
- Markdown files
- PDF documents

The included sample corpus consists of FastAPI documentation ingested directly from the official website.

---

# Design Decisions

## Why RAG?

Instead of relying solely on an LLM's pre-trained knowledge, the application retrieves relevant documentation before generating an answer. This improves factual accuracy and reduces hallucinations.

---

## Why LangGraph?

LangGraph provides a modular workflow where retrieval and generation are separated into reusable nodes. This makes the architecture easier to extend with additional steps such as reranking, conversation memory, or evaluation.

---

## Why ChromaDB?

ChromaDB is lightweight, easy to integrate, and well-suited for local vector storage during development. It provides efficient semantic retrieval without requiring an external database.

---

## Why Gemini?

Google Gemini 2.5 Flash offers fast inference, strong reasoning capabilities, and seamless integration with LangChain.

---

# Chunking Strategy

The documents are split using LangChain's Recursive Character Text Splitter.

Typical configuration:

- Chunk Size: 1000 characters
- Chunk Overlap: 200 characters

This strategy balances context preservation with retrieval accuracy while minimizing token usage.

---

# Embedding Strategy

Embeddings are generated using:

```
sentence-transformers/all-MiniLM-L6-v2
```

Reasons:

- Lightweight
- Fast inference
- High semantic similarity performance
- Suitable for local execution

---

# Workflow

1. User submits documentation.
2. Documents are loaded.
3. Text is split into chunks.
4. Chunks are embedded.
5. Embeddings are stored in ChromaDB.
6. User asks a question.
7. Retriever fetches relevant chunks.
8. LangGraph executes the workflow.
9. Gemini generates the final answer.
10. Sources are returned with the response.

---

# Future Improvements

Given more time, I would implement:

- Drag-and-drop PDF upload
- Streaming responses
- Conversation memory
- Multi-document collections
- Authentication
- Docker deployment
- Cloud deployment
- Better error handling
- Automatic source ranking

---

# Assumptions

- Documentation is available in English.
- Documents are reasonably structured.
- Users provide valid website URLs.
- The application is designed for local development.

---

# Author

**Suryaveer Singh**
