from langchain_community.llms import HuggingFaceHub

def load_llm():
    return HuggingFaceHub(
        repo_id="google/flan-t5-base",
        model_kwargs={"temperature": 0.5}
    )