def generate_response(query, db, llm):
    try:
        docs = db.similarity_search(query, k=2)

        context = " ".join([doc.page_content[:200] for doc in docs])

        prompt = f"""
        Context: {context}

        Question: {query}

        Give a short and clear answer:
        """

        response = llm.invoke(prompt)

        if hasattr(response, "content"):
            response = response.content
        else:
            response = str(response)

# 🔥 CLEAN OUTPUT
            response = response.replace(prompt, "").strip()
    
            return response
    
    except Exception as e:
            import traceback
            return f"❌ LLM Error:\n{traceback.format_exc()}"