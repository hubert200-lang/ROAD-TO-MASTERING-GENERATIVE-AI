messages=[
    ("system", "tutor instructions here")
]

print("Personal ttor assistant, type 'quit | bye | exit to end chat")

while True:
    user_input=input("Student: ")
    if user_input.lower() in ['quit', 'bye', 'exit']:
        print("Tank you for your time dude, quiting.......")
        break;
    messages.append(("humen", user_input))
    # get tutor response
    response=llm.invoke(message)
    print("thinking.............")
    print(f"Tutor: {response.content}\n")

    messages.append(("ai", response.content))