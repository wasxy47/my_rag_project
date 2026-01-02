````markdown
# 📚 Smart-RAG: Multi-Document Insight Engine

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-orange.svg)](https://aistudio.google.com/)
[![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-green.svg)](https://www.trychroma.com/)

**Smart-RAG** is a Retrieval-Augmented Generation (RAG) system designed to extract intelligent, context-aware insights from multiple text documents at once. Instead of basic keyword matching, it uses **semantic search** to understand intent and meaning, returning precise answers grounded in your source files.

---

## ✨ Key Features

- **Advanced Reasoning:** Powered by **Gemini 2.5 Flash**, leveraging structured reasoning before producing final answers.  
- **Semantic Memory:** Uses Google’s `text-embedding-004` model for high-accuracy vector representations.  
- **Multi-Document Support:** Automatically scans and indexes all `.txt` files inside the `/data` directory.  
- **Source Attribution:** Each response includes metadata indicating which document the answer came from.  
- **Persistent Vector Store:** Built on **ChromaDB**, allowing fast retrieval without reprocessing files on every run.

---

## 🛠️ Tech Stack

- **LLM:** Google Gemini 2.5 Flash  
- **Embeddings:** Google Text-Embedding-004  
- **Vector Database:** ChromaDB  
- **Backend / Orchestration:** Python (`google-genai` SDK)  
- **Text Processing:** LangChain RecursiveCharacterTextSplitter  

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure Python **3.10+** is installed. Then create and activate a virtual environment:

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
````

---

### 2. Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Environment Setup

Create a `.env` file in the project root and add your API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

---

### 4. Usage

1. Place your `.txt` files inside the `data/` directory
2. Run the application:

```bash
python main.py
```

---

## 🔍 Architecture & Workflow

1. **Ingestion & Chunking:**
   Text files are split into ~1000 character chunks with overlap to preserve context.

2. **Vectorization:**
   Each chunk is converted into a semantic embedding.

3. **Storage:**
   Embeddings and metadata (source filenames) are stored in ChromaDB.

4. **Retrieval:**
   User queries are embedded and matched against stored vectors to find the most relevant chunks.

5. **Answer Generation:**
   Retrieved context is passed to Gemini 2.5 Flash to generate accurate, document-backed responses.

---

## 📂 Project Structure

```text
my_rag_project/
├── data/               # Input text files
├── db/                 # ChromaDB persistent storage
├── .env                # API keys (ignored by Git)
├── .gitignore
├── requirements.txt
├── main.py             # App entry point
└── utils.py            # RAG logic, embeddings, DB handling
```

---

## 🤝 Contributing

Contributions are welcome.
Open an issue for discussion or submit a pull request to improve the system.

---

## 🧭 Future Roadmap

* PDF and DOCX document support
* Web-based UI (Streamlit / FastAPI)
* Hybrid search (semantic + keyword)
* Conversation memory for multi-turn Q&A
* Deployment-ready Docker setup

---

### Updating on GitHub

1. Open `README.md` in VS Code
2. Select all content and delete
3. Paste this entire block
4. Commit and push using Source Control
