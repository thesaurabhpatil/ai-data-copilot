import streamlit as st
from app.rag import load_vector_db
from app.llm import load_llm
from app.service import generate_response

st.set_page_config(page_title="AI Copilot", layout="wide")

st.title("⚡ AI Data Copilot")

# Load system
@st.cache_resource
def load_system():
    return load_vector_db(), load_llm()

db, llm = load_system()

# ---------------- SESSION STATE ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("💬 Chat History")

# New Chat button
if st.sidebar.button("➕ New Chat"):
    st.session_state.messages = []

# Show past chats
for i, (q, a) in enumerate(st.session_state.chat_history):
    if st.sidebar.button(f"{i+1}. {q[:25]}..."):
        st.session_state.messages = [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a},
        ]

# ---------------- MAIN CHAT ---------------- #

# Show messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Ask anything...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
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

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )

    # IMPORTANT: Save to history
    st.session_state.chat_history.append((user_input, full_response))