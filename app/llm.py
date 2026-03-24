from langchain_huggingface import HuggingFaceEndpoint

def load_llm():
    return HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        task="conversational",   
        temperature=0.5,
        max_new_tokens=512,
    )