````markdown
# 🚀 Smart-RAG v2.0 — Multi-Document Nexus Insight Engine

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-2.x_Flash-orange.svg)](https://aistudio.google.com/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-green.svg)](https://www.trychroma.com/)

**Smart-RAG v2.0** is a professional-grade **Retrieval-Augmented Generation (RAG)** system designed to deliver precise, context-aware answers from large document collections.  
It combines **semantic search**, **persistent vector storage**, and a **dual-data ingestion pipeline** to support both static knowledge bases and live document uploads.

---

## 🌟 What Makes This Different

Smart-RAG v2.0 is built around a **Dual-Stream Knowledge Architecture**:

1. **Pre-Fed Knowledge Base**
   - Automatically indexes all documents inside the `data/` directory on startup.
   - Ideal for textbooks, manuals, notes, and long-term reference material.

2. **Dynamic Runtime Uploads**
   - Upload **PDF, DOCX, or TXT** files directly through the Streamlit UI.
   - Instantly expands the AI’s knowledge without restarting the app.

This design supports both **stable datasets** and **ad-hoc exploration** in a single system.

---

## ✨ Key Features

- **Multi-Format Document Support**  
  Extracts and processes content from PDF, DOCX, and TXT files.

- **Semantic Search (Not Keyword Matching)**  
  Uses `text-embedding-004` to understand meaning, intent, and context.

- **Persistent Vector Memory**  
  ChromaDB stores embeddings locally for fast retrieval across sessions.

- **Source-Aware Responses**  
  Answers are generated strictly from retrieved document chunks, with file-level attribution.

- **Resilient API Handling**  
  Gracefully handles rate limits (429) and server overloads (503).

- **Modular Architecture**  
  Clean separation between UI, RAG logic, document parsing, and vector storage.

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
````

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

### Notes for GitHub

* Replace your existing `README.md` entirely with this file.
* Commit message suggestion:
  **`refactor: upgrade README for Smart-RAG v2.0`**

This README positions your project as **serious, scalable, and portfolio-ready**—the kind that recruiters and collaborators actually respect.

```

If you want next-level polish, the natural upgrades are:
- a **System Architecture diagram**
- a **demo GIF**
- a **GitHub social preview banner**

Those are the finishing touches that separate hobby repos from real engineering projects.
```