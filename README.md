# 🩺 Medical Assistant Chatbot

An AI-powered RAG (Retrieval-Augmented Generation) chatbot that lets you upload medical PDF documents and ask questions about them in natural language. Built with FastAPI, Streamlit, LangChain, Pinecone, and Google Gemini embeddings.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B)
![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C)

### 🔗 [Live Demo →](https://medical-assistant-chatbot123.streamlit.app/)

---

## ✨ Features

- 📄 **Upload multiple PDF documents** and automatically chunk, embed, and index them
- 💬 **Chat interface** to ask natural-language questions about your uploaded documents
- 🔍 **Semantic search** powered by Pinecone vector database and Google Gemini embeddings
- 🤖 **LLM-powered answers** using Groq's fast inference API
- 📚 **Source attribution** — see which document chunks were used to generate each answer
- 🚫 **Grounded responses** — the assistant only answers from your uploaded documents and won't hallucinate facts or give medical advice/diagnoses

---

## 🏗️ Architecture

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│  Streamlit  │  HTTP   │   FastAPI    │         │   Pinecone  │
│   Frontend  │ ──────► │   Backend    │ ──────► │ Vector Store│
└─────────────┘         └──────┬───────┘         └─────────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
              ┌─────▼─────┐          ┌──────▼──────┐
              │  Google   │          │    Groq     │
              │  Gemini   │          │  (LLM Chat) │
              │(Embeddings)│         └─────────────┘
              └───────────┘
```

**Flow:**
1. User uploads PDFs → text is extracted, chunked, and embedded using Google's `gemini-embedding-001`
2. Embeddings + text are stored in Pinecone (vector database)
3. User asks a question → the question is embedded and matched against stored vectors
4. Top-matching document chunks are retrieved and passed to Groq's LLM as context
5. The LLM generates a grounded answer, along with the sources used

---

## 🛠️ Tech Stack

| Layer            | Technology                              |
|-------------------|------------------------------------------|
| Frontend          | [Streamlit](https://streamlit.io)       |
| Backend API        | [FastAPI](https://fastapi.tiangolo.com) |
| Orchestration      | [LangChain](https://www.langchain.com)  |
| Vector Database    | [Pinecone](https://www.pinecone.io)     |
| Embeddings         | Google Gemini (`gemini-embedding-001`)  |
| LLM                | [Groq](https://groq.com) (`openai/gpt-oss-120b`) |
| PDF Parsing        | LangChain `PyPDFLoader`                 |

---

## 📁 Project Structure

```
MedicalAssistant/
├── client/                        # Streamlit frontend
│   ├── app.py                     # Main Streamlit entry point
│   ├── config.py                  # API URL configuration
│   ├── components/
│   │   ├── chatUI.py              # Chat interface component
│   │   ├── upload.py              # PDF upload sidebar component
│   │   └── history_download.py    # Chat history export
│   ├── utils/
│   │   └── api.py                 # API client functions
│   └── requirements.txt
│
├── server/                        # FastAPI backend
│   ├── main.py                    # FastAPI app entry point
│   ├── logger.py                  # Logging configuration
│   ├── middlewares/
│   │   └── exception_handlers.py  # Global exception handling
│   ├── modules/
│   │   ├── load_vectorstore.py    # PDF processing + Pinecone upload
│   │   ├── llm.py                 # LLM chain setup (prompt + model)
│   │   ├── query_handlers.py      # Query execution logic
│   │   └── pdf_handlers.py        # PDF utility functions
│   ├── routes/
│   │   ├── upload_pdfs.py         # POST /upload_pdfs/ endpoint
│   │   └── ask_question.py        # POST /ask/ endpoint
│   └── requirements.txt
│
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.12+
- API keys for:
  - [Google AI Studio](https://aistudio.google.com/apikey) (Gemini)
  - [Groq](https://console.groq.com/keys)
  - [Pinecone](https://app.pinecone.io)

### 1. Clone the repository

```bash
git clone https://github.com/sau1812/Medical-Assistant-Chatbot.git
cd Medical-Assistant-Chatbot
```

### 2. Set up the backend

```bash
cd server
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

Create a `.env` file inside `server/`:

```env
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_INDEX_NAME=medicalindex
```

> ⚠️ **Never commit your `.env` file.** Make sure it's listed in `.gitignore`.

Run the backend:

```bash
uvicorn main:app --reload
```

Backend will be available at `http://127.0.0.1:8000` — check `http://127.0.0.1:8000/docs` for the interactive API docs.

### 3. Set up the frontend

Open a **new terminal**:

```bash
cd client
pip install -r requirements.txt
streamlit run app.py
```

Frontend will be available at `http://localhost:8501`.

---

## 🚀 Usage

Try it live: **[medical-assistant-chatbot123.streamlit.app](https://medical-assistant-chatbot123.streamlit.app/)**

Or run it locally:

1. Open the Streamlit app in your browser
2. Use the sidebar to upload one or more medical PDF documents
3. Click **"Upload DB"** — the app will chunk, embed, and index your documents
4. Once uploaded, ask questions in the chat box (e.g. *"What is diabetes?"*)
5. View the AI-generated answer along with cited sources

---

## 🌐 Deployment

This project is deployed on [Render](https://render.com).

**Backend (FastAPI) — Render Web Service settings:**

| Setting        | Value                                              |
|-----------------|-----------------------------------------------------|
| Build Command    | `pip install -r requirements.txt`                   |
| Start Command    | `uvicorn main:app --host 0.0.0.0 --port $PORT`       |
| Environment Vars | `GOOGLE_API_KEY`, `GROQ_API_KEY`, `PINECONE_API_KEY`, `PINECONE_INDEX_NAME` |

**Frontend (Streamlit)** can be deployed separately (e.g. Streamlit Community Cloud) — update `client/config.py`'s `API_URL` to point to your deployed backend URL.

---

## 🔐 Security Notes

- API keys are loaded via environment variables (`.env` locally, dashboard env vars in production) — never hardcoded
- `.env`, `__pycache__/`, and uploaded documents are excluded from version control via `.gitignore`
- If any credentials are ever accidentally exposed, rotate them immediately from the respective provider's dashboard

---

## 📋 Known Limitations

- The assistant only answers from uploaded document context — it will not provide general medical advice or diagnoses by design
- Answer quality depends on PDF text extraction quality (scanned/image-based PDFs without OCR may not parse well)
- Embedding model output dimension (3072) must match the Pinecone index dimension — recreate the index if switching embedding models

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](../../issues).

## 📄 License

This project is open source. Add your preferred license (MIT, Apache 2.0, etc.) here.