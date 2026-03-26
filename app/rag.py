from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


# -------------------------------
# EMBEDDINGS
# -------------------------------
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# -------------------------------
# LOAD / CREATE VECTOR DB
# -------------------------------
def load_vector_db(texts=None):
    embeddings = get_embeddings()

    # If texts provided → create DB
    if texts:
        return FAISS.from_texts(texts, embeddings)

    # Else → create default dummy DB
    dummy_texts = [
        "AI is transforming the world.",
        "Python is widely used in data engineering.",
        "Machine learning is part of AI.",
    ]

    return FAISS.from_texts(dummy_texts, embeddings)