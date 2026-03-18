import streamlit as st
from app.rag import load_vector_db
from app.llm import load_llm
from app.service import generate_response

st.set_page_config(page_title="AI Copilot", layout="wide")

st.title("⚡ AI Data Copilot")

# ✅ Cache heavy components
@st.cache_resource
def load_system():
    return load_vector_db(), load_llm()

db, llm = load_system()

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
st.sidebar.title("💬 Chats")

if st.sidebar.button("➕ New Chat"):
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Ask anything...")

if user_input:
    # Show user
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            for chunk in generate_response(user_input, db, llm):
                full_response += chunk
                response_placeholder.markdown(full_response)

        except Exception as e:
            full_response = "⚠️ Error generating response"
            st.error(str(e))

    # Save
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )