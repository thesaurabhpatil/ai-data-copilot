from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

def load_llm():
    pipe = pipeline(
        "text-generation",                     
        model="distilgpt2",                    
        max_new_tokens=200,
    )

    return HuggingFacePipeline(pipeline=pipe)