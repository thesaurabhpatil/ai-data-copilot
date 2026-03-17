from app.rag import load_vector_db
from langchain_community.llms import Ollama

# Load vector DB
db = load_vector_db()

# Use lightweight model (important for your system)
llm = Ollama(model="tinyllama")

# Ask question
query = "Explain AI in simple terms"

# Step 1: Retrieve top-k documents (reranking style)
docs = db.similarity_search(query, k=3)

# Step 2: Build context (limit size for better results)
context = "\n".join([doc.page_content[:300] for doc in docs])

# Step 3: Optimized prompt
prompt = f"""
You are an AI assistant.

Use ONLY the context below to answer the question.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}

Answer in simple and clear terms:
"""

# Step 4: Call LLM
response = llm.invoke(prompt)

print("\n========== FINAL ANSWER ==========\n")
print(response)