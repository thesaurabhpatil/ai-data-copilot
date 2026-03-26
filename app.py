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
        return f"❌ Error: {str(e)}"


# -------------------------------
# CHAT FUNCTION (FAST + CLEAN)
# -------------------------------
def chat_fn(message, history):
    global pdf_db, default_db

    if not message:
        return history, ""

    try:
        active_db = pdf_db if pdf_db else default_db

        response = generate_response(message, active_db, llm)

        if not response or response.strip() == "":
            response = "⚠️ No response generated"

        history = history + [[message, response]]

        return history, ""

    except Exception as e:
        import traceback
        history = history + [[message, f"❌ Error:\n{traceback.format_exc()}"]]
        return history, ""


# -------------------------------
# UI (CHATGPT STYLE)
# -------------------------------
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("# ⚡ AI Data Copilot")
    gr.Markdown("🚀 Chat with your documents using AI (RAG powered)")

    with gr.Row():

        # LEFT PANEL
        with gr.Column(scale=1):
            gr.Markdown("### 📄 Upload PDF")

            pdf_input = gr.File(label="Upload PDF")
            upload_btn = gr.Button("Process PDF", variant="primary")
            status = gr.Textbox(label="Status", interactive=False)

            upload_btn.click(upload_pdf, inputs=pdf_input, outputs=status)

        # RIGHT PANEL (CHAT)
        with gr.Column(scale=3):

            chatbot = gr.Chatbot(height=500)

            msg = gr.Textbox(
                placeholder="Ask something...",
                show_label=False
            )

            clear = gr.Button("Clear Chat")

            msg.submit(
                chat_fn,
                inputs=[msg, chatbot],
                outputs=[chatbot, msg]
            )

            clear.click(
                lambda: [],
                None,
                chatbot,
                queue=False
            )


# -------------------------------
# LAUNCH
# -------------------------------
if __name__ == "__main__":
    demo.launch()