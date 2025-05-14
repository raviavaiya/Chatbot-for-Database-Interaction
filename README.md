# 🧠 SQL Chatbot — Natural Language to SQL Interface

This project allows users to interact with a live SQL database using natural language.  
Built with **Streamlit**, **LangChain**, and **Ollama**, this chatbot converts user questions into SQL queries and fetches results directly from the database.

---

## ✨ Features

- ✅ Ask database questions in plain English.
- 🧠 Uses Ollama + LangChain for natural language to SQL translation.
- 💬 Voice and text input supported.
- 🧱 Streamlit UI with modern sidebar navigation.
- 🔌 Connects to any SQL database (SQLite, PostgreSQL, MySQL, etc.).

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [Ollama](https://ollama.com/)
- [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu)
- [streamlit-webrtc](https://github.com/whitphx/streamlit-webrtc)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- Database: SQLite / PostgreSQL / MySQL

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/sql-chatbot.git
cd sql-chatbot

# Install dependencies
pip install -r requirements.txt

# Optional: Install FFmpeg (required for voice recognition)
# macOS: brew install ffmpeg
# Ubuntu: sudo apt install ffmpeg
# Windows: https://ffmpeg.org/download.html
