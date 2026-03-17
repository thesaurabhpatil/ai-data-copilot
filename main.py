import streamlit as st
from app.rag import load_vector_db
from langchain_community.llms import Ollama

# Page config
st.set_page_config(page_title="AI Data Copilot", layout="wide")

# Title
st.title("🤖 AI Data Copilot")

# Load DB + LLM
@st.cache_resource
def load_system():
    db = load_vector_db()
    llm = Ollama(model="tinyllama")
    return db, llm

db, llm = load_system()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("💬 Chat History")

for i, (q, a) in enumerate(st.session_state.chat_history):
    if st.sidebar.button(f"Chat {i+1}: {q[:20]}..."):
        st.session_state.messages = [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a},
        ]

# ---------------- MAIN CHAT ---------------- #

# Display messages like ChatGPT
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# Chat input (bottom like ChatGPT)
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    #  RAG logic
    docs = db.similarity_search(user_input, k=3)
    context = "\n".join([doc.page_content[:300] for doc in docs])

    prompt = f"""
    You are an AI assistant.

    Use ONLY the context below.
    If answer is not in context, say "I don't know".

    Context:
    {context}

    Question:
    {user_input}

    Answer:
    """

    response = llm.invoke(prompt)

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save messages
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.session_state.chat_history.append((user_input, response))