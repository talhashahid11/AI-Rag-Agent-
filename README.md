# 📄 AI PDF Chat (RAG App with Groq)

An interactive AI-powered application that allows you to **upload a PDF and ask questions about it** using Retrieval-Augmented Generation (RAG).

Built with ⚡ **Streamlit**, 🧠 **Sentence Transformers**, 🔍 **FAISS**, and 🚀 **Groq LLMs**.

---

## 🚀 Features

* 📄 Upload any PDF document
* 💬 Ask questions in natural language
* 🧠 Semantic search using embeddings
* ⚡ Fast responses with Groq LLM
* 🎨 Clean and interactive UI
* 📊 Context-aware answers (RAG pipeline)

---

## 🧠 How It Works

1. **PDF Upload** → Extract text from document
2. **Chunking** → Split text into smaller pieces
3. **Embeddings** → Convert chunks into vectors
4. **Vector Search (FAISS)** → Find relevant chunks
5. **LLM (Groq)** → Generate answer using context

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit 🎨
* Sentence Transformers 🤗
* FAISS 🔍
* Groq API ⚡

---

## 📦 Installation

```bash
git clone https://github.com/your-username/pdf-chat-ai.git
cd pdf-chat-ai
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Create a `.env` file or directly add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

⚠️ **Do NOT share your API key publicly**

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📸 Demo

Upload a PDF and ask questions like:

* "Summarize this document"
* "What is the main topic?"
* "Explain section 2"

---

## 📌 Example Use Cases

* 📚 Study notes summarization
* 📑 Research paper Q&A
* 🏢 Business document analysis
* 📖 Book understanding

---

## ⚡ Future Improvements

* 💬 Chat history memory
* 📂 Multiple PDF support
* 🌐 Deployment (web app)
* 🎨 Advanced UI/UX (animations)

---

## 🤝 Contributing

Feel free to fork this repo and submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
