import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("api_key"))


st.title("📄 PDF Question Answering System")


loader = PyPDFLoader("sample_rag_document.pdf")
documents = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("faiss_index")
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings
)


query = st.text_input("Ask a question about the PDF")


def ask_groq(prompt):

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content


if query:

    docs = vectorstore.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer the question based on the context below.

    Context:
    {context}

    Question:
    {query}
    """

    answer = ask_groq(prompt)

    st.write(answer)