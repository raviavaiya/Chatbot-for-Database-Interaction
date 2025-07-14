# 🍽️ Food SQLBot - Chat with Your Food Database

A **FastAPI + LangChain-powered chatbot** that lets you ask natural language questions about **Indian cuisine** and get accurate responses using **SQL over PostgreSQL** and **Google Gemini**.

---

## 🚀 Features

- Ask questions like:
  - *"How many vegetarian dishes are there?"*
  - *"List top 5 Gujarati dishes by rating"*
  - *"What dishes include Paneer?"*
- Uses Google Gemini LLM via LangChain
- Automatically generates and executes SQL queries
- Handles **case-sensitive** PostgreSQL columns
- Clean **HTML/CSS UI** with background image support
- Returns only final answer (not SQL) to end-user

---

## 🛠️ Tech Stack

- **FastAPI** – for backend API
- **LangChain** – for SQL agent and prompt handling
- **PostgreSQL** – database backend
- **SQLAlchemy** – DB connection & execution
- **Google Gemini** – LLM used via `ChatGoogleGenerativeAI`
- **HTML + CSS** – for the frontend
- **dotenv** – for loading API keys securely

---

## 📦 Installation

Follow these steps to set up and run the Food SQLBot locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/food-sqlbot.git
cd food-sqlbot

```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### 3. Install Requirements

```
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database

- Make sure PostgreSQL is running.
- Create a database named Food_Products.
- Add a table indian_food_cuisine with all required columns (like Dish_Name, Cuisine_name, etc.).

### 5. Run the App
```
uvicorn app:app --reload
```

### 🙏 Credits

Inspired by: Chat with MySQL using Python and LangChain
Built with ❤️ by Ravi Avaiya
