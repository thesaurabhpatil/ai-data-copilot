from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document

def load_vector_db():
    docs = [
        Document(page_content="AI is transforming the world"),
        Document(page_content="Python is used in data engineering"),
        Document(page_content="Machine learning is a subset of AI")
    ]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.from_documents(docs, embeddings)

    return vector_db