import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


import os 
from dotenv import load_dotenv

load_dotenv()

## langsmith Treacking
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Q&A Chatbot With OPENAI"

## prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpfull assistant. please responce to the user queries"),
        ("user","questions:{question}")
    ]
)

def generate_responce(question,api_key,llm,temperature,max_token):
    openai.api_key=api_key
    llm=ChatOpenAI(model=llm)
    out_parser=StrOutputParser()
    chain=prompt|llm|out_parser
    answer=chain.invoke({'questin':question})
    return answer