import os
from utils import process_all_books, get_semantic_context, clear_database, client
from google.genai import types

def chat_with_books():
    db_path = "./db"
    
    if not os.path.exists(db_path):
        print("First time setup: Processing all books in /data...")
        process_all_books()
        print("Processing complete!")
    
    SELECTED_MODEL = "gemini-2.5-flash" 

    print("\n" + "═"*40)
    print("   📚  SMART BOOK READER ACTIVE  📚   ")
    print("   Commands: 'exit' | 'clear'         ")
    print("═" * 40)

    while True:
        query = input("\n💬 Your Question if not then exit/quit: ").strip()
        if not query: continue
        if query.lower() == 'exit' or query.lower() == 'quit': break
        if query.lower() == 'clear':
            clear_database()
            print("Database cleared. Restart to re-process files.")
            break
        
        context = get_semantic_context(query)
        
        prompt = f"""
        Instructions:
        You are a specialized RAG assistant. Below is context retrieved from multiple files.
        Each section starts with '[Source File: filename]'. 
        If a user asks about a specific file, ONLY look at the text under that source label.

        Context:
        {context}
        
        Question: {query}
        """
        
        try:
            response = client.models.generate_content(
                model=SELECTED_MODEL, 
                contents=prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(include_thoughts=True)
                )
            )
            
            for part in response.candidates[0].content.parts:
                if part.thought:
                    # Thinking ko thora light rakhte hain
                    print(f"\n🔍 [Analyzing Context...]")
                    # print(f"{part.text}") # Agar thinking nahi dekhni to ise comment kar den
                else:
                    # Yahan humne "Gemini Answer" hata kar behtar heading daal di hai
                    print(f"\n📖 Book Insights:")
                    print(f"{part.text}")
                    print("─" * 40)
                    
        except Exception as e:
            print(f"\n⚠️ Error: {e}")

if __name__ == "__main__":
    chat_with_books()