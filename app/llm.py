from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

def load_llm():
    pipe = pipeline(
        "text2text-generation",
        model="google/flan-t5-small",   # ✅ lightweight & works
        max_new_tokens=512,
    )

    return HuggingFacePipeline(pipeline=pipe)