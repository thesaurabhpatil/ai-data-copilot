import streamlit as st
from app.rag import load_vector_db  
from app.llm import load_llm
from app.service import generate_response
from app.db import init_db, save_chat, load_chats, delete_chat, update_chat, rename_chat
from app.pdf_utils import load_pdf, split_text
from app.rag import create_vector_db

st.set_page_config(page_title="AI Copilot", layout="wide")

st.title("⚡ AI Data Copilot")

# Init DB
init_db()

# Cache system
@st.cache_resource
def load_system():
    return load_vector_db(), load_llm()

db, llm = load_system()

# ---------------- SESSION ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("💬 Chats")

# 🔍 Search
search_query = st.sidebar.text_input("🔍 Search chats")

# New Chat
if st.sidebar.button("➕ New Chat"):
    st.session_state.messages = []
    st.session_state.current_chat_id = None

# Load chats
chats = load_chats(search_query)

for chat_id, title, messages in chats:
    col1, col2, col3 = st.sidebar.columns([5,1,1])

    # Load chat
    if col1.button(title[:25], key=f"load_{chat_id}"):
        st.session_state.messages = messages
        st.session_state.current_chat_id = chat_id

    # Rename
    if col2.button("✏️", key=f"rename_{chat_id}"):
        st.session_state.rename_id = chat_id

    # Delete
    if col3.button("❌", key=f"del_{chat_id}"):
        delete_chat(chat_id)
        st.rerun()

# Rename input box
if "rename_id" in st.session_state:
    new_title = st.sidebar.text_input("Rename chat")

    if st.sidebar.button("Save Name"):
        rename_chat(st.session_state.rename_id, new_title)
        del st.session_state.rename_id
        st.rerun()

st.sidebar.header("📄 Upload PDF")

uploaded_file = st.sidebar.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    with st.spinner("Processing PDF..."):
        text = load_pdf(uploaded_file)
        docs = split_text(text)

        st.session_state.pdf_db = create_vector_db(docs)

        st.sidebar.success("PDF ready for chat!")
# ---------------- MAIN CHAT ---------------- #

# Show messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Ask anything...")

if user_input:
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

   # ---------------- RESPONSE LOGIC (FINAL) ---------------- #

# Choose active DB (PDF or default)
if "pdf_db" in st.session_state:
    active_db = st.session_state.pdf_db
else:
    active_db = db

# Generate response
with st.chat_message("assistant"):
    placeholder = st.empty()
    full_response = ""

    try:
        for chunk in generate_response(user_input, active_db, llm):
            full_response += chunk
            placeholder.markdown(full_response)
    except Exception as e:
        full_response = "⚠️ Error generating response"
        st.error(str(e))

# Save assistant message
st.session_state.messages.append(
    {"role": "assistant", "content": full_response}
)

# AVE / UPDATE CHAT (IMPORTANT)
if st.session_state.current_chat_id is None:
    # New chat
    title = user_input[:30]
    chat_id = save_chat(title, st.session_state.messages)
    st.session_state.current_chat_id = chat_id
else:
    # Existing chat → update
    update_chat(st.session_state.current_chat_id, st.session_state.messages)