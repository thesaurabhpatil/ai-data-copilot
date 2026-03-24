def generate_response(query, db, llm):
    docs = db.similarity_search(query, k=2)

    context = " ".join([doc.page_content[:200] for doc in docs])

    prompt = f"""
    Context: {context}
    Question: {query}
    Answer:
    """

    response = llm.invoke(prompt)

    # 🔥 CRITICAL FIX
    if hasattr(response, "content"):
        return response.content   # LangChain AIMessage
    else:
        return str(response)      # fallback