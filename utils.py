import os
import gc
import shutil
import time
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader
from docx import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

DB_PATH = "./db"
DATA_DIR = "./data"

def get_db_client():
    """ChromaDB client with reset enabled for Windows compatibility."""
    return chromadb.PersistentClient(
        path=DB_PATH, 
        settings=Settings(allow_reset=True) # Reset function enable karne ke liye
    )

def get_collection():
    db_client = get_db_client()
    return db_client.get_or_create_collection(name="book_collection")

def clear_database():
    """Safely wipes data using the reset method."""
    try:
        db_client = get_db_client()
        db_client.reset() # Bina folder delete kiye data clear karta hai
        gc.collect() 
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def extract_text(file_source, filename):
    text = ""
    try:
        if filename.endswith(".pdf"):
            reader = PdfReader(file_source)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted: text += extracted + "\n"
        elif filename.endswith(".docx"):
            doc = Document(file_source)
            for para in doc.paragraphs:
                text += para.text + "\n"
        else: # .txt
            if hasattr(file_source, "read"):
                if hasattr(file_source, "seek"): file_source.seek(0)
                text = file_source.read().decode("utf-8")
            else:
                with open(file_source, 'r', encoding='utf-8') as f:
                    text = f.read()
    except Exception as e:
        print(f"Extraction Error: {e}")
    return text

def process_single_file(file_source, filename):
    text = extract_text(file_source, filename)
    if not text.strip(): return False
        
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_text(text)
    collection = get_collection()
    
    for i, chunk in enumerate(chunks):
        # 429 Error se bachne ke liye gap
        time.sleep(0.5) 
        result = client.models.embed_content(model="text-embedding-004", contents=chunk)
        embedding = result.embeddings[0].values
        
        collection.add(
            ids=[f"{filename}_{i}"],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{"source": filename}]
        )
    return True

def process_all_from_folder():
    if not os.path.exists(DATA_DIR): os.makedirs(DATA_DIR)
    for filename in os.listdir(DATA_DIR):
        if filename.endswith((".txt", ".pdf", ".docx")):
            process_single_file(os.path.join(DATA_DIR, filename), filename)

def get_semantic_context(query, top_k=3): # top_k=3 tokens bachane ke liye
    collection = get_collection()
    query_result = client.models.embed_content(model="text-embedding-004", contents=query)
    query_embedding = query_result.embeddings[0].values
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    
    combined_context = ""
    if results['documents']:
        for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
            combined_context += f"\n[Source: {meta['source']}]\n{doc}\n"
    return combined_context