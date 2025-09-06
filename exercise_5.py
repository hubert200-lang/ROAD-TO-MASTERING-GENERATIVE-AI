from langchain_config import load_google_chat_model

# 1. Load chat model
chat_model = load_google_chat_model()

# 2. Create welcome interface
print("--- Welcome to the Interactive Chat! ---")
print("You can start chatting with the AI. Type 'exit', 'quit', or 'bye' to end the conversation.")

# 3. Initialize messages array with system prompt
messages = [("system", "You are a helpful assistant.")]

# 4. Implement chat loop
while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("--- Goodbye! ---")
        break

    messages.append(("user", user_input))

    print("AI: ", end="")
    full_response = ""
    for chunk in chat_model.stream(messages):
        print(chunk.content, end="", flush=True)
        full_response += chunk.content
    messages.append(("ai", full_response))
