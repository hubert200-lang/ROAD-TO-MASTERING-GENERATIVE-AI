from langchain_config import load_google_chat_model

# 1. Load chat model
chat_model = load_google_chat_model()

# 2. Create messages array with system and user messages
messages1 = [
    ("system", "You are a helpful assistant that translates English to French."),
    ("user", "I love programming.")
]

# 3. Get response using invoke()
print("--- Response from first prompt ---")
response1 = chat_model.invoke(messages1)
print(response1.content)

# 4. Test different system prompts
messages2 = [
    ("system", "You are a helpful assistant that translates English to Spanish."),
    ("user", "I love programming.")
]

print("\n--- Response from second prompt ---")
response2 = chat_model.invoke(messages2)
print(response2.content)

