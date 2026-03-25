import gradio as gr
from app.rag import create_vector_db
from app.llm import load_llm
from app.service import generate_response
from app.pdf_utils import load_pdf, split_text
import warnings
warnings.filterwarnings("ignore")
gr.close_all()
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
        return f"❌ Chat Error:\n{traceback.format_exc()}"
    
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
            status = gr.Textbox(label="Status")

        with gr.Column(scale=3):
            chat_ui = gr.ChatInterface(
                fn=chat_fn
            )

    upload_btn.click(upload_pdf, inputs=pdf_input, outputs=status)

demo.launch()