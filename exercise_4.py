from langchain_config import load_google_chat_model

# 1. Load chat model
chat_model = load_google_chat_model()

# 2. Create messages array
messages = [
    ("system", "You are a helpful assistant."),
    ("user", "Tell me a short story about a robot who discovers music.")
]

# 3. Implement streaming with stream()
print("--- Streaming response ---")
for chunk in chat_model.stream(messages):
    print(chunk.content, end="", flush=True)