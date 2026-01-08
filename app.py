import streamlit as st
import os
from utils import process_all_from_folder, process_single_file, get_semantic_context, clear_database, client
from google.genai import types

st.set_page_config(page_title="Nexus AI", page_icon="🚀", layout="wide")

# CSS Fix
st.markdown("<style>.stChatMessage { border-radius: 10px; }</style>", unsafe_allow_html=True)

st.title("🚀 Project Nexus: Document AI")

with st.sidebar:
    st.header("📂 Data Management")
    files = st.file_uploader("Upload Files", type=["pdf", "docx", "txt"], accept_multiple_files=True)
    if st.button("📥 Start Indexing"):
        if files:
            with st.spinner("Processing... Please wait."):
                for f in files: process_single_file(f, f.name)
                st.success("Indexing Done!")
    
    st.markdown("---")
    if st.button("🗑️ Clear All Memory"):
        if clear_database():
            st.session_state.messages = []
            st.success("Memory Wiped!")
            st.rerun()

if "messages" not in st.session_state: st.session_state.messages = []

# Startup Sync
if not os.path.exists("./db"):
    with st.spinner("Loading local folder..."): process_all_from_folder()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

if query := st.chat_input("Ask about your documents..."):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"): st.markdown(query)

    with st.chat_message("assistant"):
        try:
            context = get_semantic_context(query)
            # Use Flash model for higher quota
            response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=f"Context: {context}\n\nQuestion: {query}",
                config=types.GenerateContentConfig(thinking_config=types.ThinkingConfig(include_thoughts=True))
            )
            
            for part in response.candidates[0].content.parts:
                if part.thought:
                    with st.expander("🔍 Thinking Process"): st.write(part.text)
                else:
                    st.write(part.text)
                    st.session_state.messages.append({"role": "assistant", "content": part.text})
        except Exception as e:
            if "429" in str(e):
                st.error("⚠️ Quota Limit: Please wait 60 seconds.")
            elif "503" in str(e):
                st.error("⚠️ Server Busy: Google is overloaded. Try again in a bit.")
            else:
                st.error(f"Error: {e}")