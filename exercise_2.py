from langchain_config import load_google_llm

# 1. Load the model
llm = load_google_llm()

# 2. Create a prompt
prompt = "Tell me about the history of the internet."

# 3. Get response using invoke()
print("--- Response from invoke() ---")
response = llm.invoke(prompt)
print(response)

# 4. Implement streaming with stream()
print("\n--- Response from stream() ---")
for chunk in llm.stream(prompt):
    print(chunk, end="", flush=True)
