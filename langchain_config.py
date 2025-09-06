# config.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()

def load_google_llm(model="gemini-2.5-flash", temperature=0.7, max_output_tokens=2000):
    '''Loads the Google completion model.'''
    return GoogleGenerativeAI(
        model=model,
        temperature=temperature,
        max_output_tokens=max_output_tokens,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

def load_google_chat_model(model="gemini-2.5-flash", temperature=0.7, max_output_tokens=2000):
    '''Loads the Google chat model.'''
    return ChatGoogleGenerativeAI(
        model=model,
        temperature=temperature,
        max_output_tokens=max_output_tokens,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

def load_groq_chat_model(model="llama3-8b-8192", temperature=0.7, max_output_tokens=2000):
    '''Loads the Groq chat model.'''
    return ChatGroq(
        model=model,
        temperature=temperature,
        max_tokens=max_output_tokens,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )
