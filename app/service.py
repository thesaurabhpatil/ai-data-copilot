def generate_response(query, db, llm):
    try:
        docs = db.similarity_search(query, k=3)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a helpful AI assistant.

Use ONLY the context below to answer.
If answer is not in context, say "I don't know".

Context:
{context}

Question:
{query}

Answer in 2-3 sentences:
"""

        response = llm.invoke(prompt)

        if hasattr(response, "content"):
            response = response.content
        else:
            response = str(response)

        # 🔥 Clean output
        response = response.replace(prompt, "").strip()

        # 🔥 Add sources
        sources = "\n\nSources:\n"
        for i, doc in enumerate(docs):
            sources += f"{i+1}. {doc.page_content[:100]}...\n"

        return response + sources

    except Exception as e:
        import traceback
        return f"❌ Error:\n{traceback.format_exc()}"