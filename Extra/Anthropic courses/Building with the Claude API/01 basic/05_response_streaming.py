from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"

messages = []

user_message = input("> ")
messages.append({"role": "user", "content": user_message})

with client.messages.stream(
    model=model,
    max_tokens=100,
    messages=messages,
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

final_message = stream.get_final_message()
messages.append({"role": "assistant", "content": final_message.content[0].text})
