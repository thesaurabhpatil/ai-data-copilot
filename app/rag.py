from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from config import EMBEDDING_MODEL

def load_vector_db():
    docs = [
        Document(page_content="AI is transforming the world"),
        Document(page_content="Python is used in data engineering"),
        Document(page_content="Machine learning is a subset of AI")
    ]

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return FAISS.from_documents(docs, embeddings)