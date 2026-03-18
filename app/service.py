def generate_response(query, db, llm, top_k=2, max_chars=150):
    # Step 1: Retrieve
    docs = db.similarity_search(query, k=top_k)

    # Step 2: Build context safely
    context = " ".join([
        doc.page_content[:max_chars] for doc in docs
    ])

    # Step 3: Prompt
    prompt = f"""
    Context: {context}
    Question: {query}
    Answer:
    """

    # Step 4: Generate response
    return llm.stream(prompt)