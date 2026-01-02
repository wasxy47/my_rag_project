# 📚 Smart Multi-Book RAG Assistant

A simple Retrieval-Augmented Generation (RAG) system using **Gemini 2.5 Flash** and **ChromaDB**. 

## Features
- Semantic search using Google's `text-embedding-004`.
- Multi-document support (processes all `.txt` files in `/data`).
- "Thinking" process visualization.

## Setup
1. Clone the repo.
2. Install requirements: `pip install -r requirements.txt`.
3. Add your `GEMINI_API_KEY` in a `.env` file.
4. Put your text files in the `data/` folder.
5. Run `python main.py`.