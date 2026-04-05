import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from groq import Groq

# ✅ MUST BE FIRST
st.set_page_config(page_title="PDF Chat AI", page_icon="📄")

# 🎨 STYLE
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}
.stTextInput input {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ================= INIT =================
client = Groq(api_key="paste your Api key here")
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# ================= FUNCTIONS =================
def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def split_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def get_embeddings(chunks):
    return embed_model.encode(chunks)

def create_vector_store(embeddings):
    embeddings = np.array(embeddings).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index

def retrieve(query, index, chunks):
    query_embedding = embed_model.encode([query]).astype("float32")
    _, indices = index.search(query_embedding, 3)
    return [chunks[i] for i in indices[0]]

def ask_groq(context, question):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion:\n{question}"
        }]
    )
    return response.choices[0].message.content

# ================= UI =================
st.title("📄 AI PDF Chat")
st.markdown("Upload a PDF and ask anything ✨")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    if "index" not in st.session_state:
        with st.spinner("Processing PDF..."):
            text = load_pdf(uploaded_file)
            chunks = split_text(text)
            embeddings = get_embeddings(chunks)
            index = create_vector_store(embeddings)

            st.session_state.chunks = chunks
            st.session_state.index = index

    query = st.text_input("Ask a question")

    if query:
        with st.spinner("Thinking..."):
            context = "\n".join(
                retrieve(query, st.session_state.index, st.session_state.chunks)
            )
            answer = ask_groq(context, query)

        st.markdown("### 🤖 Answer")
        st.write(answer)
