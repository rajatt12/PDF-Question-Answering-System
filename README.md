# 📄 PDF Question Answering System (Mini RAG)

An AI-powered application that allows users to **ask questions about a PDF document and receive intelligent answers** using **Retrieval Augmented Generation (RAG)**.

This project demonstrates how **Large Language Models (LLMs)** can be combined with **vector databases and embeddings** to build real-world AI applications.

---

# 🚀 Project Overview

The **PDF Question Answering System** enables users to:

1. Upload a PDF document
2. Ask questions related to the document
3. Retrieve relevant content from the PDF
4. Generate accurate answers using an LLM

Instead of letting the model guess answers, the system **retrieves relevant text from the PDF first** and then generates a response. This technique is called **Retrieval Augmented Generation (RAG)**.

---

# 🧠 How It Works (Architecture)

```
PDF Document
     │
     ▼
Text Extraction
     │
     ▼
Text Chunking
     │
     ▼
Embeddings Generation
     │
     ▼
Vector Database (FAISS)
     │
     ▼
User Question
     │
     ▼
Semantic Search
     │
     ▼
Relevant Chunks Retrieved
     │
     ▼
LLM Generates Final Answer
```

---

# 🛠️ Tech Stack

| Technology             | Purpose                                  |
| ---------------------- | ---------------------------------------- |
| Python                 | Core programming language                |
| LangChain              | Framework for building LLM pipelines     |
| FAISS                  | Vector database for similarity search    |
| HuggingFace Embeddings | Convert text into vector representations |
| PyPDF                  | Extract text from PDF files              |
| OpenAI / LLM           | Generate answers from retrieved context  |
| Streamlit              | Build interactive web interface          |

---

# 📂 Project Structure

```
pdf-question-answering-rag
│
├── app.py
├── document.pdf
├── requirements.txt
├── README.md
└── utils.py (optional helper functions)
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/pdf-question-answering-rag.git
cd pdf-question-answering-rag
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install langchain faiss-cpu pypdf streamlit sentence-transformers openai
```

---

# ▶️ Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 📑 Usage

1. Upload or place a **PDF document** in the project directory
2. Run the application
3. Enter a question about the PDF
4. The system will retrieve relevant information and generate an answer

Example questions:

```
What is supervised learning?
Explain the conclusion of the paper.
What are the key findings of this document?
```

---

# 🔍 Key Concepts Used

### 1️⃣ Text Chunking

Large documents are divided into smaller chunks so they can be processed efficiently.

### 2️⃣ Embeddings

Text is converted into numerical vectors using embedding models.

### 3️⃣ Vector Search

The system finds text chunks that are **semantically similar** to the user's query.

### 4️⃣ Retrieval Augmented Generation (RAG)

Instead of relying only on the LLM’s memory, the model uses **retrieved context from the document** to generate answers.

---

# 📊 Example Workflow

```
User Question:
"What is supervised learning?"

Step 1 → Convert question to embedding
Step 2 → Search vector database
Step 3 → Retrieve top relevant text chunks
Step 4 → Send chunks + question to LLM
Step 5 → Generate final answer
```

---

# 📈 Future Improvements

Possible enhancements for this project:

* Support **multiple PDF uploads**
* Add **chat history**
* Show **sources / citations**
* Use **advanced vector databases** like Pinecone or Weaviate
* Implement **local LLMs using Ollama**
* Add **document highlighting**
* Deploy using **Docker / Cloud**

---

# 🎯 Learning Outcomes

By building this project you learn:

* Retrieval Augmented Generation (RAG)
* Vector databases
* Embeddings and semantic search
* LangChain pipelines
* LLM application development
* Building AI-powered tools

---

# 📸 Example Use Cases

* Research paper assistant
* Legal document analysis
* Academic study helper
* Knowledge base search
* AI document assistant

---

# 👨‍💻 Author

Developed by **Rajatveer Singh**

---

# ⭐ If you found this project useful

Give the repository a ⭐ on GitHub to support the project.
