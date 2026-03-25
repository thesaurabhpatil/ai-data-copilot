import gradio as gr
from app.rag import load_vector_db
from app.llm import load_llm
from app.service import generate_response
from app.pdf_utils import load_pdf, split_text

# -------------------------------
# GLOBAL STATE
# -------------------------------
pdf_db = None
default_db = load_vector_db()
llm = load_llm()

# -------------------------------
# PDF PROCESSING
# -------------------------------
def upload_pdf(file):
    global pdf_db

    if file is None:
        return "❌ Please upload a PDF"

    try:
        text = load_pdf(file.name)
        chunks = split_text(text)

        pdf_db = load_vector_db(chunks)

        return "✅ PDF processed successfully!"

    except Exception as e:
        return f"❌ Error processing PDF: {str(e)}"


# -------------------------------
# CHAT FUNCTION (RAG)
# -------------------------------
def chat_fn(message, history):
    global pdf_db, default_db

    try:
        active_db = pdf_db if pdf_db else default_db

        response = generate_response(message, active_db, llm)

        if not response or response.strip() == "":
            return "⚠️ No response generated"

        return response

    except Exception as e:
        import traceback
        return f"❌ Error:\n{traceback.format_exc()}"


# -------------------------------
# UI
# -------------------------------
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("# ⚡ AI Data Copilot")
    gr.Markdown("Chat with your data using RAG (PDF + AI)")

    with gr.Row():

        # LEFT PANEL (PDF Upload)
        with gr.Column(scale=1):
            gr.Markdown("### 📄 Upload Document")

            pdf_input = gr.File(label="Upload PDF")
            upload_btn = gr.Button("Process PDF", variant="primary")
            status = gr.Textbox(label="Status", interactive=False)

            upload_btn.click(
                upload_pdf,
                inputs=pdf_input,
                outputs=status
            )

        # RIGHT PANEL (CHAT)
        with gr.Column(scale=3):

            chat_ui = gr.ChatInterface(
                fn=chat_fn,
                title="💬 Chat with your data",
                description="Ask questions from your PDF or knowledge base",
                examples=[
                    "What is AI?",
                    "Summarize this document",
                    "What are key insights?"
                ],
            )

# -------------------------------
# LAUNCH
# -------------------------------
if __name__ == "__main__":
    demo.launch()