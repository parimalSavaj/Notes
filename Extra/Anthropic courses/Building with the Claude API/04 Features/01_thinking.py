from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic
client = Anthropic()

def chat(messages, thinking=False, thinking_budget=1024): # thinking budget must greater then or equal to 1024!
    params = {
        "model": "claude-sonnet-4-0",
        "messages": messages,
        "max_tokens": 2000
    }

    if thinking:
        params["thinking"] = {
            "type": "enabled",
            "budget_tokens": thinking_budget
        }

    response = client.messages.create(**params)

    return response

messages = [
    {"role": "user", "content": "Explain why binary search is efficient"}
]

# response = chat(messages, thinking=False)
response = chat(messages, thinking=True)
print(response)