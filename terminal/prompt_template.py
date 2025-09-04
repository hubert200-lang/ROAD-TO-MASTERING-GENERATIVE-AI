# PROMTP TEMPLATE HELPS INTEGRATE VCARIABLES - LOGIC INTO PROMPT

from langchain_core.prompts import PromptTemplate
from config import connect_to_llm, environment_settings

environment_settings()

llm=connect_to_llm()

prompt_templates=PromptTemplate.from_template(
    "Give me a summay of this book: {book} writen by author: {author}"
)

book=input("Enter your favourite book title: ")
author=input("Also 😂, please the author of your book: ")
print("_"*79)


template=prompt_templates.format(
    book=book,
    author=author
)
print("Loading.........🌟🌟🌟")

res=llm.invoke(template)
print(res)