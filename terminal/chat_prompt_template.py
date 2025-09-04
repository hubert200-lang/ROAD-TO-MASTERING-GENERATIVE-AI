from langchain_core.prompts import ChatPromptTemplate
from config import connect_to_llm, environment_settings
environment_settings()
llm=connect_to_llm()
chat_template=ChatPromptTemplate.from_messages(
    [
        ("system", " you are an {expert} in {field}"),
        ("human","Hello, {expert} my name is {name}, please answer this question"),
        ("ai","Sure...."),
        ("human", "{user_input}")
    ]
)

# Take user Inputs

profession=input("What should I sound like today?   ")
name=input(f"\n AI⛑: Okay nice, I will assume the {profession} title given, what should i call you? ")
user_input=input("What should i then do for you? ")

field=input("What is your field of expertise? Before I forget😂 ")

# pass inputs as templates

chat_prompt_templates=chat_template.format_messages(
    expert=profession,
    name=name,
    user_input=user_input,
    field=field
)

print("Loading........🌟🌟 🌟")
res=llm.invoke(chat_prompt_templates)
print(res)