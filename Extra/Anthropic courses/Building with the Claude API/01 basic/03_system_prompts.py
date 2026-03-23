from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"
system_prompt = """
You are a patient math tutor.
You will help the student understand how to solve math problems by breaking them down into smaller steps and providing clear explanations. You will also ask the student questions to check their understanding and encourage them to think critically about the problem. Your goal is to help the student learn and improve their math skills, not just give them the answer.
"""

def add_user_message(messages, content):
    messages.append({"role": "user", "content": content})

def add_assistant_message(messages, content):
    messages.append({"role": "assistant", "content": content})

def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 100,
        "messages": messages,
    }

    if system is not None:
        params["system"] = system # why because system prompt goes None so we get error 

    response = client.messages.create(**params)

    return response.content[0].text


messages = []

while True:
    # user message
    user_input = input("> ")

    # add user message to conversation history
    add_user_message(messages, user_input)

    # get assistant response
    assistant_response = chat(messages, system_prompt)

    # add assistant response to conversation history
    add_assistant_message(messages, assistant_response)

    # print assistant response
    print("Assistant:", assistant_response)