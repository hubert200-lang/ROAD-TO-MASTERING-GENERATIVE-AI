from langchain_config import load_google_llm
from langchain_core.prompts import PromptTemplate

# 1. Load the model
llm = load_google_llm()

# 2. Create templates
book_summary_template = PromptTemplate.from_template(
    "Write a short summary of the book '{title}' by {author}."
)

recipe_template = PromptTemplate.from_template(
    "Provide a recipe for {cuisine} cuisine that includes the following ingredients: {ingredients}."
)

learning_template = PromptTemplate.from_template(
    "Explain the topic of '{topic}' at a {difficulty} level."
)

# 3. Main loop
while True:
    print("\n--- Choose an application ---")
    print("1. Book Summary Generator")
    print("2. Recipe Generator")
    print("3. Learning Explainer")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\n--- Book Summary Generator ---")
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        prompt = book_summary_template.format(title=title, author=author)
        print("\n--- Generating summary ---")
        response = llm.invoke(prompt)
        print(response)

    elif choice == '2':
        print("\n--- Recipe Generator ---")
        cuisine = input("Enter the cuisine type (e.g., Italian, Mexican): ")
        ingredients = input("Enter the ingredients (comma-separated): ")
        prompt = recipe_template.format(cuisine=cuisine, ingredients=ingredients)
        print("\n--- Generating recipe ---")
        response = llm.invoke(prompt)
        print(response)

    elif choice == '3':
        print("\n--- Learning Explainer ---")
        topic = input("Enter the topic to explain: ")
        difficulty = input("Enter the difficulty level (e.g., beginner, intermediate, expert): ")
        prompt = learning_template.format(topic=topic, difficulty=difficulty)
        print("\n--- Generating explanation ---")
        response = llm.invoke(prompt)
        print(response)

    elif choice == '4':
        print("--- Goodbye! ---")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
