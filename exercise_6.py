from langchain_config import load_google_llm
from langchain_core.prompts import PromptTemplate

# 1. Load the model
llm = load_google_llm()

# 2. Create a template
template = PromptTemplate.from_template(
    "Write a short summary of the book '{title}' by {author}."
)

# 3. Get user input
print("--- Book Summary Generator ---")
title = input("Enter the book title: ")
author = input("Enter the author's name: ")

# 4. Format the prompt and get a response
prompt = template.format(title=title, author=author)

print("\n--- Generating summary ---")
summary = llm.invoke(prompt)
print(summary)
