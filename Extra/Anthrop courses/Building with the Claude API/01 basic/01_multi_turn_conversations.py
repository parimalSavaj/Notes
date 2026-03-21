from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"

def add_user_message(messages, content):
    messages.append({"role": "user", "content": content})

def add_assistant_message(messages, content):
    messages.append({"role": "assistant", "content": content})

def chat(messages):
    response = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return response.content[0].text

# Example conversation
messages = []
add_user_message(messages, "Hello! Can you tell me a joke?")
print("User: Hello! Can you tell me a joke?")
assistant_response = chat(messages)
add_assistant_message(messages, assistant_response)
print("Assistant:", assistant_response)

add_user_message(messages, "That's funny! Can you tell me another one?")
print("\nUser: That's funny! Can you tell me another one?")
assistant_response = chat(messages)
add_assistant_message(messages, assistant_response)
print("Assistant:", assistant_response)

