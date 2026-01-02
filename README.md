[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-orange.svg)](https://aistudio.google.com/)
[![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-green.svg)](https://www.trychroma.com/)

# 📚 Smart-RAG: Multi-Document Insight Engine

**Smart-RAG** is a sophisticated Retrieval-Augmented Generation (RAG) system built to provide intelligent insights from multiple text documents simultaneously. Unlike traditional keyword searches, this engine leverages **Semantic Search** to understand the context and intent behind your questions, providing precise answers backed by specific source files.

---

## ✨ Key Features

* **Advanced Reasoning:** Powered by **Gemini 2.5 Flash**, utilizing the "Thinking" mode to provide transparent internal reasoning before the final answer.
* **Semantic Memory:** Uses Google’s `text-embedding-004` model to map text into a high-dimensional vector space for high-accuracy retrieval.
* **Multi-Book Capability:** Automatically scans and indexes all `.txt` files within the `/data` directory.
* **Source Attribution:** Each answer includes metadata tracking, allowing the AI to identify exactly which file (e.g., `book_1.txt` or `book_2.txt`) the information originated from.
* **Persistent Vector Store:** Integrated with **ChromaDB** to store embeddings locally, ensuring fast performance without re-processing documents on every run.

---

## 🛠️ Tech Stack

* **LLM:** Google Gemini 2.5 Flash
* **Embeddings:** Google Text-Embedding-004
* **Vector Database:** ChromaDB
* **Orchestration:** Python with `google-genai` SDK
* **Text Processing:** LangChain RecursiveCharacterTextSplitter

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python 3.10 or higher installed. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

```

### 2. Installation

Install the necessary dependencies:

```bash
pip install -r requirements.txt

```

### 3. Environment Setup

Create a `.env` file in the root directory and add your Google AI Studio API Key:

```env
GEMINI_API_KEY=your_actual_api_key_here

```

### 4. Usage

Place your text files in the `data/` folder and launch the application:

```bash
python main.py

```

---

## 🔍 Architecture & Workflow

1. **Ingestion & Chunking:** The system reads all text files and breaks them into 1,000-character segments with a 100-character overlap to preserve context.
2. **Vectorization:** Each chunk is converted into a numerical vector (embedding) representing its semantic meaning.
3. **Storage:** Vectors and their associated metadata (filenames) are stored in a local ChromaDB instance.
4. **Semantic Retrieval:** When a query is entered, the system calculates the query's vector and retrieves the top-k most relevant chunks from the database.
5. **Contextual Generation:** The retrieved text is fed into Gemini 2.5 Flash as context, producing a highly accurate, document-grounded response.

---

## 📂 Project Structure

```text
my_rag_project/
├── data/               # Input text files/books
├── db/                 # Local ChromaDB persistent storage
├── .env                # Secret API keys
├── .gitignore          # Prevents sensitive data from being pushed to Git
├── requirements.txt    # Project dependencies
├── main.py             # User interface and execution flow
└── utils.py            # RAG logic, embeddings, and DB management

```

---

### How to Apply this to GitHub:

1. Open your `README.md` in VS Code.
2. Delete the existing text and paste the content above.
3. **Save** the file.
4. Go to the **Source Control** tab, type a commit message like `docs: complete rewrite of readme in English`, and click **Commit & Sync**.

**Would you like me to add a "Future Roadmap" section to the README? This shows recruiters that you have a plan to improve the project with features like PDF support or a Web UI.**
