import os
from dotenv import load_dotenv, find_dotenv
import datetime

from langchain_google_genai import GoogleGenerativeAI

load_dotenv(find_dotenv())
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = GoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7, api_key=GOOGLE_API_KEY)
# res=llm.invoke("Sing a ballad of LangChain.")

# WRITE A SIMPLE FUNCTION CALLED=> daily_journal

# mood and the event the day: so ai is now going to give you a reflection
# and what you need to do to improve your day

# they are going to be stored in a text file

def daily_journal():
    # Project header
    print("welcome to my Daily Journal App 😁")
    print("_"*50)
    # Get input from the user:
    mood=input("What happened today? \n")
    event=input("How was your mood today? \n")

    prompt=f"Help me reflect on my day. Today, {mood}. I felt {event}. Provide a brief reflection and suggest one way I can improve tomorrow."

    print("REFLECTION from Ai: ")
    print("_"*50)
    for part in llm.stream(prompt):
        print(part, end="", flush=True)
    with open("daily_journal.txt", "a") as f:
        f.write(f"\n{datetime.date.today()} \n")
        f.write(f"\nDay Reflection:\nMood: {mood}\nEvent: {event}\n")
        f.write("AI Reflection:\n")
        for part in llm.stream(prompt):
            f.write(part)
        f.write("\n" + "_"*50 + "\n")

# call our function here
daily_journal()

    


