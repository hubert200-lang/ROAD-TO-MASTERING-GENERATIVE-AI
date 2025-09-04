# Exercises for GenAI Developers

A practical collection of hands-on exercises focused on mastering LangChain fundamentals. Learn to build AI applications using completion models, chat models, prompt templates, and chat prompt templates with popular LLM providers.

## Purpose

This repository provides structured learning exercises for developers getting started with LangChain and Generative AI. Each exercise builds upon previous concepts, guiding you from basic LLM interactions to sophisticated prompt engineering and conversational AI systems.

## Prerequisites

- Python 3.8 or higher
- Basic Python programming knowledge
- API keys from supported providers (Google AI, Groq)

## Installation and Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/exercises-for-genai-devs.git
cd exercises-for-genai-devs
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env file and add your API keys
```

4. Create your configuration file:
Create a `config.py` file in the root directory following the pattern shown in the exercises.

## Exercise Structure

Each exercise includes:
- **Objective**: Clear learning goals
- **Concepts**: Key concepts covered
- **Instructions**: Step-by-step guidance
- **Starter Code**: Boilerplate to begin with
- **Expected Output**: What you should see when complete
- **Challenge**: Extension activities for deeper learning

---

## Exercise 1: Setting Up LangChain Configuration

**Objective**: Create a reusable configuration module for LangChain models

**Concepts**: Environment management, Model initialization, Code organization

### Instructions

1. Create a `config.py` file that loads different LLM providers
2. Implement functions to load Google AI and Groq models
3. Use environment variables for API key management
4. Test your configuration with a simple model call

### Starter Code Structure

```python
# config.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()

def load_google_llm():
    # TODO: Implement Google completion model loader
    pass

def load_google_chat_model():
    # TODO: Implement Google chat model loader
    pass

def load_groq_chat_model():
    # TODO: Implement Groq chat model loader
    pass
```

### What You Should Learn
- How to organize LangChain configurations
- Environment variable management
- Different model types (completion vs chat)
- API key security practices

### Challenge
Add error handling for missing API keys and create a model selector function.

---

## Exercise 2: Your First LLM Completion

**Objective**: Use a completion model to generate text responses

**Concepts**: LLM completion, Basic prompting, Streaming responses

### Instructions

1. Load a Google completion model using your config
2. Create a simple prompt about a topic you're interested in
3. Get a response using the `invoke()` method
4. Implement streaming to see the response generated in real-time

### Starter Code

```python
from config import load_google_llm

# TODO: Load the model
# TODO: Create a prompt
# TODO: Get response using invoke()
# TODO: Implement streaming with stream()
```

### Expected Behavior
- See immediate response with invoke()
- Watch text appear word-by-word with streaming
- Handle the response content properly

### Challenge
Create a simple loop that accepts user prompts and responds using the completion model.

---

## Exercise 3: Basic Chat Model Interaction

**Objective**: Build conversational interactions using chat models

**Concepts**: Chat models, Message formatting, System prompts, Conversation flow

### Instructions

1. Load a Google chat model from your config
2. Create a message structure with system and user roles
3. Use the chat model to respond to questions
4. Experiment with different system prompts to change AI behavior

### Starter Code

```python
from config import load_google_chat_model

# TODO: Load chat model
# TODO: Create messages array with system and user messages
# TODO: Get response using invoke()
# TODO: Test different system prompts
```

### Expected Message Format
```python
messages = [
    ("system", "You are a helpful assistant specialized in..."),
    ("user", "Your question here")
]
```

### Challenge
Create different personas by changing the system message and test how responses change.

---

## Exercise 4: Streaming Chat Responses

**Objective**: Implement real-time streaming for chat interactions

**Concepts**: Streaming responses, Real-time output, User experience optimization

### Instructions

1. Use your chat model from the previous exercise
2. Implement streaming using the `stream()` method
3. Handle the streaming output to display smoothly
4. Add proper formatting and user experience elements

### Key Implementation

```python
# Streaming pattern
for part in chat_model.stream("Your question"):
    print(part.content, end="", flush=True)
```

### What to Focus On
- Smooth text appearance
- Proper output formatting
- Handling empty content parts
- User experience considerations

### Challenge
Add a typing indicator or progress visualization while streaming.

---

## Exercise 5: Interactive Chat Loop

**Objective**: Build a continuous conversation interface

**Concepts**: While loops, User input handling, Exit conditions, Chat flow

### Instructions

1. Create a welcome message and interface
2. Implement a while loop for continuous conversation
3. Handle user input and model responses
4. Add proper exit conditions and cleanup

### Starter Code

```python
from config import load_google_chat_model

chat_model = load_google_chat_model()

# TODO: Create welcome interface
# TODO: Initialize messages array with system prompt
# TODO: Implement chat loop
# TODO: Handle exit conditions
```

### Features to Implement
- Welcome message with clear instructions
- Professional interface design
- Multiple exit commands (exit, quit, bye)
- Proper goodbye message

### Challenge
Add conversation history management to maintain context across multiple exchanges.

---

## Exercise 6: Prompt Templates Fundamentals

**Objective**: Create reusable, dynamic prompts using PromptTemplate

**Concepts**: Template creation, Variable substitution, Prompt engineering, Code reusability

### Instructions

1. Import and use LangChain's PromptTemplate
2. Create a template with multiple variables
3. Accept user input for template variables
4. Format and execute the template with a completion model

### Template Pattern

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "Your template string with {variable1} and {variable2}"
)
```

### Application Ideas
- Book summarization with title and author
- Recipe generation with ingredients and cuisine
- Learning explanations with topic and difficulty level

### Challenge
Create a template validator that ensures all required variables are provided.

---

## Exercise 7: Advanced Prompt Templates with Multiple Inputs

**Objective**: Build sophisticated prompt templates with multiple parameters

**Concepts**: Complex templating, Input validation, User experience design

### Instructions

1. Design a prompt template with 4+ variables
2. Create a user-friendly input collection process
3. Add loading indicators and professional formatting
4. Use streaming for better user experience

### Suggested Template Themes
- Tutorial generator (topic, audience, length, format)
- Product description creator (product, features, target audience, tone)
- Story writer (genre, characters, setting, length)

### Professional Touch
- Clear input prompts
- Loading indicators
- Formatted output presentation
- Error handling for invalid inputs

### Challenge
Add input validation and smart defaults for optional parameters.

---

## Exercise 8: Chat Prompt Templates

**Objective**: Master conversational prompt templates with multiple message types

**Concepts**: ChatPromptTemplate, Multi-role conversations, Context building

### Instructions

1. Use ChatPromptTemplate.from_messages()
2. Create templates with system, user, and AI message roles
3. Include multiple variables across different message types
4. Build a complex conversational context

### Template Structure

```python
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an {role} specialized in {domain}..."),
    ("user", "Previous context or example..."),
    ("ai", "Example AI response with {variable}..."),
    ("user", "{main_user_input}")
])
```

### Implementation Focus
- Role-based conversation design
- Context building through multiple messages
- Variable distribution across message types
- Professional conversation flow

### Challenge
Create a template that maintains conversation context while allowing for dynamic topic changes.

---

## Exercise 9: Expert System with Chat Templates

**Objective**: Build a sophisticated expert system using advanced chat templates

**Concepts**: Expert system design, Domain specialization, Professional AI personas

### Instructions

1. Create a comprehensive expert system template
2. Include multiple conversation turns with context
3. Use variables to customize expertise and domain
4. Implement professional conversation management

### System Design
- Expert role definition
- Domain specialization
- Conversation history
- Professional response patterns

### Features to Implement
- Dynamic expert selection
- Domain-specific knowledge activation
- Context-aware responses
- Professional interaction patterns

### Challenge
Add memory management to maintain conversation context across multiple expert consultations.

---

## Exercise 10: Interactive Application Builder

**Objective**: Combine all concepts into a complete interactive application

**Concepts**: Application architecture, User experience, Feature integration

### Instructions

1. Create a menu-driven application interface
2. Integrate completion models, chat models, and templates
3. Provide multiple interaction modes
4. Include proper error handling and user guidance

### Application Features
- Multiple AI interaction modes
- Template-based conversations
- Streaming and non-streaming options
- Professional user interface
- Comprehensive error handling

### Architecture Components
- Configuration management
- Model selection system
- Template library
- User interface layer
- Error handling system

### Challenge
Add conversation export functionality and session management.

---

## Project Structure

```
exercises-for-genai-devs/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── config.py
├── exercises/
│   ├── exercise_01_setup/
│   │   ├── README.md
│   │   ├── starter.py
│   │   └── solution.py
│   ├── exercise_02_completion/
│   │   ├── README.md
│   │   ├── starter.py
│   │   └── solution.py
│   └── [other exercises...]
├── solutions/
│   ├── config_solution.py
│   ├── exercise_01_solution.py
│   └── [other solutions...]
└── resources/
    ├── templates/
    └── examples/
```

## Learning Path

### Phase 1: Foundation (Exercises 1-3)
Master basic LangChain setup, model loading, and simple interactions.

### Phase 2: Interaction Patterns (Exercises 4-5)
Learn streaming, conversation loops, and user experience design.

### Phase 3: Template Mastery (Exercises 6-8)
Advanced prompt engineering and template-based AI interactions.

### Phase 4: Integration (Exercises 9-10)
Build complete applications combining all learned concepts with professional Streamlit interfaces.

## Streamlit Development Guidelines

### Essential Components
Each Streamlit application should include:

```python
# Standard imports and setup
import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import load_google_chat_model, load_google_llm

# Page configuration
st.set_page_config(
    page_title="Exercise Name",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Session state initialization
if "messages" not in st.session_state:
    st.session_state.messages = []
```

### UI Design Patterns

**Sidebar Configuration**
```python
with st.sidebar:
    st.title("Configuration")
    model_choice = st.selectbox("Choose Model:", ["Google", "Groq"])
    temperature = st.slider("Temperature:", 0.0, 1.0, 0.7)
    max_tokens = st.number_input("Max Tokens:", 100, 4000, 2000)
```

**Chat Interface**
```python
# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Process and respond
```

**Streaming Implementation**
```python
# Streaming response in Streamlit
with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""
    
    for chunk in model.stream(prompt):
        full_response += chunk.content
        message_placeholder.markdown(full_response + "▌")
    
    message_placeholder.markdown(full_response)
```

### Advanced Features
- **File Upload**: `st.file_uploader()` for document processing
- **Data Display**: `st.dataframe()`, `st.json()` for structured data
- **Metrics**: `st.metric()` for performance indicators  
- **Progress**: `st.progress()`, `st.spinner()` for loading states
- **Layout**: `st.columns()`, `st.expander()`, `st.tabs()` for organization

## Common Patterns and Best Practices

### Configuration Management
```python
# Always use environment variables for API keys
# Create reusable model loading functions
# Handle missing credentials gracefully
```

### Error Handling
```python
# Check for API key availability
# Handle network timeouts
# Manage rate limiting
# Validate user inputs
```

### User Experience
```python
# Provide clear instructions
# Use loading indicators
# Format output professionally
# Handle edge cases gracefully
```

## Troubleshooting

### Common Issues
1. **Missing API Keys**: Ensure .env file is properly configured
2. **Import Errors**: Verify all required packages are installed
3. **Rate Limiting**: Implement proper delays between requests
4. **Token Limits**: Monitor and handle context window limitations

### Getting Help
- Check exercise README files for specific guidance
- Review solution files for implementation examples
- Test with simple examples before building complex features

## Contributing

We welcome contributions that align with our focused approach:

1. **Exercise Contributions**: Add exercises using the established patterns
2. **Solution Improvements**: Enhance existing solutions with better practices
3. **Documentation**: Improve clarity and add helpful examples
4. **Bug Fixes**: Report and fix issues in existing code

### Contribution Guidelines
- Follow the established exercise format
- Include comprehensive documentation
- Test all code before submitting
- Focus on practical, hands-on learning

## Next Steps

After completing these exercises, you'll have solid foundations in:
- LangChain configuration and setup
- Completion and chat model usage
- Prompt template design and implementation
- Professional AI application development

Consider exploring:
- Advanced LangChain features (agents, chains)
- Vector databases and RAG systems
- Production deployment patterns
- Integration with web frameworks

---

**Start your journey with Exercise 1 and build your GenAI development skills step by step.**