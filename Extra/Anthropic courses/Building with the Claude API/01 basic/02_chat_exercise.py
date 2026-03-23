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
        max_tokens=100,
        messages=messages,
    )
    return response.content[0].text


messages = []

while True:
    # user message
    user_input = input("> ")

    # add user message to conversation history
    add_user_message(messages, user_input)

    # get assistant response
    assistant_response = chat(messages)

    # add assistant response to conversation history
    add_assistant_message(messages, assistant_response)

    # print assistant response
    print("Assistant:", assistant_response)