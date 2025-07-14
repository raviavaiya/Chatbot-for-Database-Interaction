from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from sqlalchemy import text
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import re
from dotenv import load_dotenv
app = FastAPI()
# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# PostgreSQL database connection
postgres_uri = "postgresql+psycopg2://postgres:root@localhost:5432/Food_Products"
db = SQLDatabase.from_uri(postgres_uri, include_tables=["indian_food_cuisine"])

# LLM configuration
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# SQL prompt template
template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
SQL Query:"""
prompt = ChatPromptTemplate.from_template(template)

# SQL generation chain
sql_chain = (
    RunnablePassthrough.assign(schema=lambda x: x["db"].get_table_info())
    | prompt
    | llm.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)

# SQL execution utility
sensitive_identifiers = [
    "indian_food_cuisine", "id", "Diet_Type", "Course_name", "Discrption_of_Dish",
    "Cuisine_name", "Ratings_of_Dish", "Ingredients_of_Dish", "Prepration_time",
    "Cooking_time", "Total_time", "Makes", "Recipe_Instructions", "Dish_Name"
]

def execute_sql_query(query: str):
    try:
        query = re.sub(r"```sql|```", "", query).strip()
        sensitive_identifiers = [
            "indian_food_cuisine", "id", "Diet_Type", "Course_name", "Discrption_of_Dish",
            "Cuisine_name", "Ratings_of_Dish", "Ingredients_of_Dish", "Prepration_time",
            "Cooking_time", "Total_time", "Makes", "Recipe_Instructions", "Dish_Name"
        ]
        for ident in sensitive_identifiers:
            query = re.sub(rf'(?<!\")\b{ident}\b(?!\")', f'"{ident}"', query)

        with db._engine.connect() as conn:
            result = conn.execute(text(query))
            rows = result.fetchall()
            if not rows:
                return "No results found."
            result_rows = [", ".join(str(value) for value in row._mapping.values()) for row in rows]
            result_text = "\n".join(result_rows)
            return f"✅ Answer:\n{result_text}"
    except Exception as e:
        return f"❌ SQL Execution Error: {e}"

# FastAPI app initialization


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/ask")
async def ask_sql(request: Request):
    body = await request.json()
    question = body.get("question", "")
    sql_query = sql_chain.invoke({"question": question, "db": db})
    result = execute_sql_query(sql_query)
    return JSONResponse(content={"answer": result})
