def environment_settings():
    import os
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    # print the keys
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    print(f"Google API Key: {GOOGLE_API_KEY}")  
    print(f"Groq API Key: {GROQ_API_KEY}")

def connect_to_llm():
    from langchain_google_genai import GoogleGenerativeAI
    llm=GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    return llm
def connect_to_llm_chat():
    from langchain_google_genai import ChatGoogleGenerativeAI
    llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    return llm
def connect_to_groq():
    from langchain_groq import ChatGroq
    llm=ChatGroq(model="deepseek-r1-distill-llama-70b", temperature=0.7)
    return llm

def connect_to_db_url():
    import os
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    DATABASE_URL = os.getenv("DATABASE_URL")
    print(f"Database URL: {DATABASE_URL}")
    return DATABASE_URL