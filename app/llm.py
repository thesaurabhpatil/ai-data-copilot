from langchain_huggingface import HuggingFaceEndpoint

def load_llm():
    return HuggingFaceEndpoint(
        repo_id="google/flan-t5-base",
        temperature=0.5,
        max_new_tokens=512
    )