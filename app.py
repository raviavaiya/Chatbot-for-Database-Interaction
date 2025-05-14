import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_option_menu import option_menu


# Sidebar layout
with st.sidebar:
    st.title("SQL Chatbot Settings")
    selected = option_menu(
        menu_title="Main Menu",       # required
        options=["Chat", "Settings", "About"],  # required
        icons=["chat", "gear", "info-circle"],  # optional
        menu_icon="cast",             # optional
        default_index=0,              # optional
    )

    add_vertical_space(2)
    add_vertical_space(15)
    st.write("Made with ❤️ by [Ravi Avaiya](https://raviavaiya-portfolio.vercel.app/)")

# Functions for each page
def show_chat():
    st.header("💬 Chat with Database")
    user_query = st.text_input("Ask something about your Database:")
    if user_query:
        st.write(f"You asked: **{user_query}**")
        # You can add LLM and SQL logic here

def show_settings():
    st.header("⚙️ Settings")
    st.write("Configure your chatbot here:")
    st.checkbox("Show SQL queries")
    st.selectbox("Choose LLM model", ["Ollama", "OpenAI", "Local"])

def show_about():
    st.header("📖 About this App")
    st.markdown('''
    This chatbot converts natural language questions into SQL queries and executes them on your database.

    **Built with:**
    - Streamlit
    - LangChain
    - Ollama
    ''')

# Routing
if selected == "Chat":
    show_chat()
elif selected == "Settings":
    show_settings()
elif selected == "About":
    show_about()
