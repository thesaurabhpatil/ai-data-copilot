import gradio as gr
from app.rag import create_vector_db
from app.llm import load_llm
from app.service import generate_response
from app.pdf_utils import load_pdf, split_text

# Load default system
llm = load_llm()

# Global DBs
default_db = None
pdf_db = None

# ---------------- INIT DEFAULT DB ---------------- #
def init_default_db():
    global default_db

    docs = split_text(
        "AI is transforming the world. Python is widely used in data engineering. Machine learning is part of AI."
    )

    default_db = create_vector_db(docs)

init_default_db()

# ---------------- CHAT FUNCTION ---------------- #
def chat(user_input, history):
    global pdf_db, default_db

    if not user_input:
        return history, history

    try:
        if history is None:
            history = []

        active_db = pdf_db if pdf_db else default_db

        response = ""
        for chunk in generate_response(user_input, active_db, llm):
            response += chunk

        history.append((user_input, response))

        return history, history

    except Exception as e:
        history.append((user_input, f"❌ Error: {str(e)}"))
        return history, history
    
# ---------------- PDF UPLOAD ---------------- #
def upload_pdf(file):
    global pdf_db

    if file is None:
        return "❌ Please upload a file first"

    try:
        text = load_pdf(file)

        if not text.strip():
            return "❌ Could not extract text from PDF"

        docs = split_text(text)
        pdf_db = create_vector_db(docs)

        return "✅ PDF processed successfully!"

    except Exception as e:
        return f"❌ Error: {str(e)}"
    
# ---------------- UI ---------------- #
with gr.Blocks() as demo:
    gr.Markdown("# ⚡ AI Data Copilot")

    with gr.Row():
        with gr.Column(scale=1):
            pdf_input = gr.File(label="Upload PDF")
            upload_btn = gr.Button("Process PDF")
            status = gr.Textbox(label="Status", interactive=False)

        with gr.Column(scale=3):
            chatbot = gr.Chatbot()
            msg = gr.Textbox(placeholder="Ask something...")
            clear = gr.Button("Clear Chat")

    upload_btn.click(upload_pdf, inputs=pdf_input, outputs=status)
    msg.submit(chat, inputs=[msg, chatbot], outputs=[chatbot, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()