
<div align="center">

# 🧠 Local AI Study Assistant

### Privacy-First AI Learning with Local Language Models and RAG

A locally powered intelligent study companion that helps students understand technical concepts, analyze PDF documents, and generate context-aware answers using a Small Language Model (SLM).

**Built with Python, Streamlit, Ollama, Qwen2.5, and Retrieval-Augmented Generation.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-black?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Semantic%20Retrieval-green?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

[**GitHub Repository**](https://github.com/shrutisinghchauhan/Ai---Study-Assistant-)

</div>

---

## 🌟 Project Overview

**Local AI Study Assistant** is a privacy-focused AI learning application designed to make studying more interactive, intelligent, and accessible.

The application combines a locally deployed Small Language Model with Retrieval-Augmented Generation (RAG), allowing users to upload study materials, ask natural-language questions, and receive answers informed by relevant passages from their documents.

Unlike cloud-dependent AI assistants, the application performs inference and document processing locally using Ollama.

### 🎯 Problem Statement

Students frequently work with large volumes of academic material, including lecture notes, textbooks, research papers, and technical documentation.

Traditional search tools rely heavily on keyword matching, making it difficult to retrieve relevant information when questions are phrased differently from the source material.

This project addresses that challenge by integrating semantic retrieval with local language-model inference.

### 💡 Proposed Solution

The system:

1. Extracts text from uploaded PDF documents.
2. Divides documents into overlapping text chunks.
3. Generates semantic embeddings using all-minilm.
4. Retrieves relevant chunks using cosine similarity.
5. Passes retrieved context to Qwen2.5 1.5B.
6. Generates natural-language responses.
7. Displays retrieved passages and source page numbers.
8. Stores conversation history locally using SQLite.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🤖 Local AI Chatbot | Qwen2.5 1.5B powered by Ollama |
| 📄 PDF Question Answering | Ask questions directly from uploaded documents |
| 🔎 Semantic Search | Retrieve relevant content using embeddings |
| 🧠 Retrieval-Augmented Generation | Combine document context with LLM inference |
| 📚 Source References | Display relevant PDF passages and page numbers |
| 💬 Conversation Memory | Persistent SQLite-based chat history |
| 🔍 Chat Search | Search previously saved conversations |
| ⚙️ Configurable Settings | Adjust retrieval count and generation limits |
| 📊 Performance Monitoring | Measure response time, token count, and throughput |
| 🔐 Privacy-Focused | Local inference without external AI APIs |
| 🎨 Modern Interface | Custom Streamlit UI with pastel styling |

---


## 🏗️ System Architecture

## 🏗️ System Architecture

```text
                  ┌───────────────────────┐
                  │         USER          │
                  └───────────┬───────────┘
                              │
                              ▼
                  ┌───────────────────────┐
                  │   STREAMLIT INTERFACE │
                  └───────────┬───────────┘
                              │
                   ┌──────────┴──────────┐
                   │                     │
                   ▼                     ▼
          ┌─────────────────┐   ┌─────────────────┐
          │  GENERAL QUERY  │   │    PDF QUERY    │
          └────────┬────────┘   └────────┬────────┘
                   │                     │
                   │                     ▼
                   │            ┌─────────────────┐
                   │            │ PDF EXTRACTION  │
                   │            └────────┬────────┘
                   │                     ▼
                   │            ┌─────────────────┐
                   │            │ TEXT CHUNKING   │
                   │            └────────┬────────┘
                   │                     ▼
                   │            ┌─────────────────┐
                   │            │ EMBEDDING MODEL │
                   │            │   all-minilm    │
                   │            └────────┬────────┘
                   │                     ▼
                   │            ┌─────────────────┐
                   │            │ COSINE SIMILARITY│
                   │            └────────┬────────┘
                   │                     ▼
                   │            ┌─────────────────┐
                   │            │ RETRIEVED TEXT  │
                   │            └────────┬────────┘
                   │                     │
                   ▼                     ▼
                  ┌───────────────────────┐
                  │    QWEN2.5 1.5B      │
                  │       OLLAMA          │
                  └───────────┬───────────┘
                              ▼
                  ┌───────────────────────┐
                  │   GENERATED ANSWER    │
                  └───────────────────────┘

                  SQLite stores chat history.
```

### Architecture Components

**Streamlit:** User interface for questions and PDF uploads.

**PyMuPDF:** Extracts document text.

**all-minilm:** Generates semantic embeddings.

**Cosine Similarity:** Retrieves relevant document passages.

**Qwen2.5 1.5B:** Generates answers locally through Ollama.

**SQLite:** Stores conversation history and metrics.

---
---
### Architecture Components

**1. User Interface**

Streamlit provides an interactive interface for uploading PDF files, asking questions, viewing responses, and managing conversations.

**2. Document Processing**

PyMuPDF extracts text from PDF documents. Sentence-aware chunking divides the extracted content into overlapping passages.

**3. Embedding Generation**

The all-minilm model converts text passages into dense vector representations.

**4. Semantic Retrieval**

Cosine similarity compares question embeddings with document embeddings to retrieve the most relevant passages.

**5. Language Model Inference**

Qwen2.5 1.5B generates responses using Ollama. For document-based questions, the retrieved passages are included in the model's context.

**6. Persistent Storage**

SQLite stores conversation messages, timestamps, document associations, and performance metrics.

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| Frontend Framework | Streamlit |
| Small Language Model | Qwen2.5 1.5B |
| Model Runtime | Ollama |
| Embedding Model | all-minilm |
| Document Processing | PyMuPDF |
| Vector Similarity | NumPy / Cosine Similarity |
| Database | SQLite |
| Data Visualization | Matplotlib |
| Version Control | Git and GitHub |

---

## 📊 Performance Evaluation

The local inference pipeline was evaluated using a benchmark of 10 requests.

### Model Performance

| Metric | Result |
|--------|--------|
| Model | Qwen2.5 1.5B |
| Successful Requests | 10/10 |
| Average Response Latency | 8.43 seconds |
| Average Generation Speed | 24.62 tokens/second |
| Inference Environment | Local Ollama |

**Note:** Successful requests indicate that the inference pipeline executed successfully. They do not establish factual accuracy. Performance depends on the local hardware and workload.

### RAG Evaluation

The project also includes a comparison of responses generated with and without document retrieval.

The evaluation workflow supports:

- Comparing RAG and non-RAG answers.
- Recording question-level results.
- Analyzing document-grounded responses.
- Visualizing evaluation outcomes.

---

## 📸 Application Screenshot

### Local AI Study Assistant — Main Interface

## 📸 Application Screenshot

### Local AI Study Assistant — Main Interface

![Local AI Study Assistant Dashboard](Screenshot%202026-10-28%20161532.png)

The interface includes:

- PDF upload and study materials management.
- Local AI model configuration.
- A conversational study assistant.
- Searchable conversation history.
- Configurable generation settings.
- A custom cream-and-sage interface.

---

## 🚀 Getting Started

### Prerequisites

Install the following:

- Python 3.12 or later
- Ollama
- Git

### Step 1 — Clone the Repository

```bash
git clone https://github.com/shrutisinghchauhan/Ai---Study-Assistant-.git
cd Ai---Study-Assistant-
```

### Step 2 — Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3 — Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4 — Download the Language Model

```bash
ollama pull qwen2.5:1.5b
```

### Step 5 — Download the Embedding Model

```bash
ollama pull all-minilm
```

### Step 6 — Run the Application

```bash
python -m streamlit run app.py
```

Open the application at:

**http://localhost:8501**

---

## 📂 Project Structure

```text
Local-AI-Study-Assistant/
│
├── assets/
│   ├── assistant.png
│   └── Screenshot 2026-10-28 161532.png
│
├── app.py
├── rag_utils.py
├── wix_inspired_theme.py
├── test_model.py
├── evaluate_model.py
├── evaluate_rag.py
├── analyze_results.py
├── requirements.txt
├── README.md
├── .gitignore
└── study_assistant.db  # Local only, excluded from Git
```

### Important Files

| File | Responsibility |
|------|----------------|
| `app.py` | Main Streamlit application |
| `rag_utils.py` | PDF processing, embeddings, and retrieval |
| `wix_inspired_theme.py` | Custom UI styling |
| `test_model.py` | Basic model functionality testing |
| `evaluate_model.py` | Model inference benchmarking |
| `evaluate_rag.py` | RAG and non-RAG comparison |
| `analyze_results.py` | Evaluation analysis and visualization |

---

## 🔒 Privacy and Security

The application follows a local-first architecture.

- LLM inference runs through locally installed Ollama.
- Document embeddings are generated locally.
- PDF processing occurs on the user's computer.
- Conversations are saved in a local SQLite database.
- No external AI inference API is required.

The local database and private study documents should be excluded from version control.

---

## 🌐 Deployment

This project is designed to run locally.

**Application URL:**

```text
http://localhost:8501
```

**GitHub Repository:**

https://github.com/shrutisinghchauhan/Ai---Study-Assistant-

GitHub hosts the source code, while Streamlit and Ollama run on the user's computer.

GitHub Pages cannot execute the Python backend or Ollama inference.

---

## 🔮 Future Enhancements

- [ ] Support multiple PDF documents simultaneously
- [ ] Persistent vector indexing
- [ ] Streaming AI responses
- [ ] Automated citation verification
- [ ] Improved RAG evaluation
- [ ] Docker-based local deployment
- [ ] Quantized model performance comparison
- [ ] Enhanced document search and filtering
- [ ] Automated testing and CI/CD

---

## 👩‍💻 Author

**Shruti Chauhan**

Integrated B.Tech + M.Tech in Information Technology

ABV-IIITM Gwalior

[GitHub Profile](https://github.com/shrutisinghchauhan)

---

<div align="center">

### Built with Python, Local AI, and Retrieval-Augmented Generation

**Privacy-First • Document-Grounded • Local AI**

</div>
