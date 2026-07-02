# if we want to generate json type structured data only!!

from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"

messages = []

# user_message = input("> ")
# messages.append({"role": "user", "content": user_message})
# ! messages.append({"role":"assistant", "content": "```json"})

# def chat(messages, stop=None):
#     response = client.messages.create(
#         model=model,
#         max_tokens=100,
#         messages=messages,
#         stop_sequences=stop,
#     )
#     return response.content[0].text

# text = chat(messages,stop=["```"])

# print(text)


#! other example
#? How can you obtain three different commands in a single response using only the specified techniques?

messages.append({"role":"user", "content": "Give instructions for obtaining three different commands in a single model response"})
messages.append({"role":"assistant", "content":"Here are all three commands in a single block without any comments\n ```bash"}) #! this assistant starting message is based LLM gives without comments in single respose.
