import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

# Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot With OPENAI"

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries."),
        ("user", "Question: {question}")
    ]
)

# Response generator function
def generate_response(question, api_key, llm_model, temperature, max_token):
    openai.api_key = api_key
    llm = ChatOpenAI(model=llm_model, temperature=temperature, max_tokens=max_token)
    out_parser = StrOutputParser()
    chain = prompt | llm | out_parser
    answer = chain.invoke({'question': question})
    return answer

# App title
st.title("Enhanced Q&A Chatbot with OpenAI")

# Sidebar settings
st.sidebar.title("Settings")
api_key = st.secrets["OPENAI_API_KEY"]
llm_model = st.sidebar.selectbox("Select an OpenAI Model", ["gpt-4o", "gpt-4-turbo", "gpt-4"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# User input
st.write("Go ahead and ask any question:")
user_input = st.text_input("You:")

if user_input:
    if api_key:
        response = generate_response(user_input, api_key, llm_model, temperature, max_tokens)
        st.write("🤖:", response)
    else:
        st.warning("⚠️ Please enter your OpenAI API key.")
else:
    st.info("📝 Please enter a question to get started.")
