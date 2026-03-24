def generate_response(query, db, llm):
    try:
        docs = db.similarity_search(query, k=2)

        context = " ".join([doc.page_content[:200] for doc in docs])

        prompt = f"""
        Answer the question using the context below.

        Context:
        {context}

        Question:
        {query}

        Answer:
        """

        response = llm.invoke(prompt)

        # 🔥 HANDLE ALL CASES
        if isinstance(response, str):
            return response

        if hasattr(response, "content"):
            return response.content

        return str(response)

    except Exception as e:
        return f"❌ LLM Error: {str(e)}"