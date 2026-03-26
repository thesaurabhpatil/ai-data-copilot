from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

def load_llm():
    pipe = pipeline(
        "text-generation",
        model="distilgpt2",      # ⚡ fastest
        max_new_tokens=120,
        temperature=0.3,
    )

    return HuggingFacePipeline(pipeline=pipe)