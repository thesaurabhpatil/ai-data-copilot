---
title: AI Data Copilot
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
---

# ⚡ AI Data Copilot (RAG + PDF Chat)

A **production-ready GenAI application** that allows you to chat with your data using **Retrieval-Augmented Generation (RAG)** and uploaded PDFs.

---

## 🚀 Features

- ⚡ Fast semantic search using FAISS  
- 🧠 Context-aware answers using RAG  
- 📄 Upload PDF & chat with documents  
- 💬 ChatGPT-like interface (Gradio UI)  
- 🌐 Deployed on Hugging Face Spaces (FREE)  
- 🧩 Modular architecture (production-ready)

---

## 🏗️ Architecture
---
title: AI Data Copilot
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.31.0
app_file: app.py
python_version: 3.10
pinned: false
---

# ⚡ AI Data Copilot (RAG + PDF Chat)

A **production-ready GenAI application** that allows you to chat with your data using **Retrieval-Augmented Generation (RAG)** and uploaded PDFs.

---

## 🚀 Features

- ⚡ Fast semantic search using FAISS  
- 🧠 Context-aware answers using RAG  
- 📄 Upload PDF & chat with documents  
- 💬 ChatGPT-like interface (Gradio UI)  
- 🌐 Deployed on Hugging Face Spaces (FREE)  
- 🧩 Modular architecture (production-ready)

---

## 🏗️ Architecture
User Query
↓
Vector DB (FAISS)
↓
Relevant Context Retrieval
↓
LLM (HuggingFace Hosted Model)
↓
Answer

---

## 📁 Project Structure
ai-data-copilot/
│
├── app.py # Gradio UI (entry point)
├── requirements.txt
├── README.md
│
├── app/
│ ├── rag.py
│ ├── llm.py
│ ├── service.py
│ └── pdf_utils.py

---

## ⚙️ Local Setup (Optional)

### 1️⃣ Clone repo
git clone https://github.com/thesaurabhpatil/ai-data-copilot

cd ai-data-copilot

---

### 2️⃣ Install dependencies
pip install -r requirements.txt

---

### 3️⃣ Set Hugging Face token
setx HUGGINGFACEHUB_API_TOKEN "your_token"
---

### 4️⃣ Run app
python app.py
---

## 🌐 Live Demo

👉 Hosted on Hugging Face Spaces (Free Deployment)

---

## 💡 Tech Stack

- Python  
- LangChain  
- FAISS  
- HuggingFace Transformers  
- Gradio  
- PyPDF  

---

## 🧠 Problem Statement

Built a modular **RAG-based AI assistant** capable of retrieving context from documents and generating accurate responses using vector search and LLMs. Designed for scalability, modularity, and real-world data use cases.

---

## 🚀 Future Improvements

- Multi-document support  
- Chat memory across sessions  
- Source citation highlighting   
- Authentication & multi-user support  

---

## 👨‍💻 Author

**Saurabh Patil**