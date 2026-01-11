import os
import time
from utils import (
    process_all_from_folder, # Updated function name from utils.py
    get_semantic_context, 
    clear_database, 
    client
)
from google.genai import types

def chat_with_books():
    db_path = "./db"
    
    # Syncing local library if database folder is missing
    if not os.path.exists(db_path):
        print("First time setup: Processing all books in /data...")
        process_all_from_folder() 
        print("Processing complete!")
    
    # Using 2.0-flash for better stability on free tier
    SELECTED_MODEL = "gemini-2.0-flash" 

    print("\n" + "═"*40)
    print("   📚  NEXUS SMART READER (v2.0)  📚   ")
    print("   Commands: 'exit' | 'clear'         ")
    print("═" * 40)

    while True:
        query = input("\n💬 Your Question (exit/quit to stop): ").strip()
        if not query: continue
        if query.lower() in ['exit', 'quit']: break
        
        if query.lower() == 'clear':
            if clear_database():
                print("✅ Database wiped using reset method.")
            else:
                print("⚠️ Error: Files are locked by Windows.")
            break
        
        # Retrieval with top_k=3 to save tokens
        context = get_semantic_context(query, top_k=3)
        
        prompt = f"""
        Instructions: Use the provided context to answer. 
        Each section starts with '[Source File: filename]'.

        Context:
        {context}
        
        Question: {query}
        """
        
        try:
            print("\n🔍 Searching through your library...")
            response = client.models.generate_content(
                model=SELECTED_MODEL, 
                contents=prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(include_thoughts=True)
                )
            )
            
            # Displaying thoughts and insights
            for part in response.candidates[0].content.parts:
                if part.thought:
                    print(f"\n🧠 [AI Thinking...]")
                else:
                    print(f"\n📖 Book Insights:")
                    print(f"{part.text}")
                    print("─" * 40)
                    
        except Exception as e:
            # Handling common API errors
            if "429" in str(e):
                print("\n⚠️ Quota Limit: Please wait 60 seconds before asking again.")
            elif "503" in str(e):
                print("\n⚠️ Server Busy: Google is overloaded. Try again in 30 seconds.")
            else:
                print(f"\n⚠️ System Error: {e}")

if __name__ == "__main__":
    chat_with_books()