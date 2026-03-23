---
title: AI Data Copilot
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.31.0
app_file: app.py
pinned: false
---
# ⚡ AI Data Copilot (RAG + Local LLM)

A **production-ready GenAI application** that allows you to chat with your data using **Retrieval-Augmented Generation (RAG)**.

Built with:

* 🧠 **FAISS** (vector database)
* 🔍 **HuggingFace Embeddings**
* 🤖 **Ollama (Local LLM - TinyLLaMA)**
* 🎨 **Streamlit UI**

---

## 🚀 Features

* ⚡ Fast semantic search using FAISS
* 🧠 Context-aware answers using RAG
* 💬 ChatGPT-like UI with streaming responses
* 🔒 Fully local (no API cost)
* 🧩 Modular architecture (production-ready)

---

## 🏗️ Architecture

User Query → FAISS Retriever → Context → LLM (Ollama) → Answer

---

## 📁 Project Structure

```
ai-data-copilot/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── app/
│   ├── rag.py
│   ├── llm.py
│   └── service.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone repo

```
git clone <https://github.com/thesaurabhpatil/ai-data-copilot>
cd ai-data-copilot
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Install Ollama

Download: https://ollama.com

---

### 4️⃣ Pull model

```
ollama pull tinyllama
```

---

### 5️⃣ Run app

```
streamlit run main.py
```

---

## 🐳 Run with Docker

```
docker build -t ai-copilot .
docker run -p 8501:8501 ai-copilot
```

---

## 💡 Tech Stack

* Python
* LangChain
* FAISS
* HuggingFace Transformers
* Streamlit
* Ollama


##  🧠 Problem Statement 

Built a modular RAG system with FAISS vector store, HuggingFace embeddings, and local LLM via Ollama. Optimized for performance using caching, streaming responses, and prompt engineering.

##  🚀 Future Improvements

PDF / API data ingestion
Multi-user authentication
Azure deployment
Chat memory


##  👨‍💻 Author

Saurabh Patil