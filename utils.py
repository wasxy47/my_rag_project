import os
import shutil
import chromadb
from dotenv import load_dotenv
from google import genai
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

DB_PATH = "./db"
DATA_DIR = "./data"

def get_collection():
    chroma_client = chromadb.PersistentClient(path=DB_PATH)
    return chroma_client.get_or_create_collection(name="book_collection")

def clear_database():
    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH)
        print("Database cleared successfully.")
        return True
    return False

def process_all_books():
    """Folder mein maujood sari txt files ko read karke DB mein dalta hai."""
    if not os.path.exists(DATA_DIR):
        print("Data folder not found!")
        return False
    
    collection = get_collection()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    
    # Har file ko bari bari read karna
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".txt"):
            file_path = os.path.join(DATA_DIR, filename)
            print(f"Processing: {filename}...")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            
            chunks = splitter.split_text(text)
            
            for i, chunk in enumerate(chunks):
                result = client.models.embed_content(
                    model="text-embedding-004",
                    contents=chunk
                )
                embedding = result.embeddings[0].values
                
                # Metadata mein filename add kar rahe hain taake pata chale 
                # ke ye information kis book se aayi hai
                collection.add(
                    ids=[f"{filename}_{i}"],
                    embeddings=[embedding],
                    documents=[chunk],
                    metadatas=[{"source": filename}]
                )
    return True

def get_semantic_context(query, top_k=5):
    collection = get_collection()
    query_result = client.models.embed_content(model="text-embedding-004", contents=query)
    query_embedding = query_result.embeddings[0].values
    
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    
    combined_context = ""
    # Results se document aur uska metadata (filename) nikalna
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        combined_context += f"\n[Source File: {meta['source']}]\n{doc}\n"
    
    return combined_context