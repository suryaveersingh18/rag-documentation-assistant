# RAG Technical Documentation Assistant

A Retrieval-Augmented Generation (RAG) application built using FastAPI, LangGraph, Gemini, ChromaDB, Hugging Face Embeddings, and Streamlit.

## Features

- Ask questions about technical documentation
- Website documentation ingestion
- Semantic search with ChromaDB
- Gemini-powered answers
- Source citations
- FastAPI REST API
- Streamlit Chat UI

## Tech Stack

- Python
- FastAPI
- LangGraph
- Google Gemini
- ChromaDB
- HuggingFace Embeddings
- Streamlit

## Installation

```bash
git clone <repository-url>
cd RAG

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
LLM_MODEL=gemini-2.5-flash
```

Run backend:

```bash
uvicorn main:app --reload
```

Run frontend:

```bash
streamlit run frontend/app.py
```

## API

- GET `/health`
- POST `/chat`
- POST `/ingest`

## Folder Structure

```
RAG/
│
├── app/
├── frontend/
├── scripts/
├── database/
├── documents/
├── requirements.txt
├── README.md
└── main.py
```