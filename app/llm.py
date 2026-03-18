from langchain_community.llms import Ollama
from config import MODEL_NAME

def load_llm():
    return Ollama(model=MODEL_NAME)