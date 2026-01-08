# 🚀 Smart-RAG v2.0 — Multi-Document Nexus Insight Engine

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-2.x_Flash-orange.svg)](https://aistudio.google.com/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-green.svg)](https://www.trychroma.com/)

**Smart-RAG v2.0** is a production-ready **Retrieval-Augmented Generation (RAG)** system engineered to deliver accurate, context-aware answers from large and diverse document collections.  
It integrates **semantic search**, **persistent vector storage**, and a **dual-data ingestion pipeline**, enabling seamless interaction with both static knowledge bases and dynamically uploaded documents.

---

## 🌟 What Makes This Different

Smart-RAG v2.0 is architected around a **Dual-Stream Knowledge Model**:

1. **Pre-Fed Knowledge Base**
   - Automatically scans and indexes all documents in the `data/` directory at startup.
   - Optimized for textbooks, manuals, notes, and long-term reference content.

2. **Dynamic Runtime Uploads**
   - Upload **PDF, DOCX, or TXT** files directly through the Streamlit interface.
   - Instantly augments the AI’s knowledge without requiring an application restart.

This approach enables both **reliable long-term storage** and **on-demand exploration** within a unified system.

---

## ✨ Key Features

- **Multi-Format Document Support**  
  Extracts and processes content from PDF, DOCX, and TXT files with consistent normalization.

- **Semantic Search (Beyond Keywords)**  
  Leverages `text-embedding-004` to capture intent, meaning, and contextual relevance.

- **Persistent Vector Memory**  
  Uses ChromaDB for local, persistent embedding storage across sessions.

- **Source-Aware Responses**  
  Generates answers strictly from retrieved document chunks, with clear file-level attribution.

- **Resilient API Handling**  
  Includes safeguards for API rate limits (429) and transient server errors (503).

- **Modular Architecture**  
  Maintains a clean separation of concerns between UI, RAG logic, document parsing, and vector storage.

---

## 🛠️ Tech Stack

- **LLM:** Google Gemini Flash (2.x series)
- **Embeddings:** Google `text-embedding-004`
- **Vector Database:** ChromaDB (Persistent, Local)
- **Frontend:** Streamlit
- **Backend / Orchestration:** Python + Google GenAI SDK
- **Text Processing:** LangChain RecursiveCharacterTextSplitter

---

## 🚀 Getting Started

### 1. Prerequisites

- Python **3.10+**
- Virtual environment recommended

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

---

### 2. Installation

```bash
pip install -r requirements.txt
```

---

### 3. Environment Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

---

### 4. Run the Application

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

---

## 🔍 Architecture & Workflow

1. **Ingestion & Chunking**
   Documents are split into ~1000-character chunks with overlap to preserve context.

2. **Vectorization**
   Each chunk is converted into a high-dimensional semantic embedding.

3. **Storage**
   Embeddings and metadata (source filename) are stored in ChromaDB.

4. **Retrieval**
   User queries are embedded and matched against stored vectors.

5. **Generation**
   Retrieved context is passed to Gemini Flash to generate grounded, factual responses.

---

## 📂 Project Structure

```text
my_rag_project/
├── app.py              # Streamlit UI & chat logic
├── utils.py            # RAG engine, parsers, DB handling
├── data/               # Pre-fed local documents
├── db/                 # ChromaDB persistent storage
├── .env                # API keys (git-ignored)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧭 Roadmap

* Conversation memory (multi-turn context)
* Hybrid search (semantic + keyword)
* Advanced metadata filtering
* FastAPI backend for production deployment
* Dockerized deployment pipeline

---

## 🤝 Contributing

Contributions are welcome.
Open an issue for discussion or submit a pull request with clear context and scope.

---

## 📌 Versioning

* **v1.x:** CLI-based, TXT-only RAG engine
* **v2.0:** Streamlit UI, multi-format ingestion, dual-data pipeline

---
