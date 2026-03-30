from dotenv import load_dotenv
from anthropic import Anthropic
from anthropic.types import ToolParam

load_dotenv()

client = Anthropic()
model = "claude-sonnet-4-5"

SYSTEM_PROMPT = """
You are an expert conversation analyst.

Your job is to analyze chat conversations and provide:
1. Sentiment (positive, negative, neutral)
2. Key insights
3. Risks (if any)
4. Summary

Always return clear structured answers.
"""

tools = [
    ToolParam(
        {
            "name": "get_current_datetime",
            "description": "Get current date and time",
            "input_schema": {
                "type": "object",
                "properties": {},
            },
        }
    ),
    ToolParam(
        {
            "name": "dummy_analysis_helper",
            "description": "Helper tool for analysis",
            "input_schema": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"],
            },
        }
    ),
]

def chat(messages, system=None, tools=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if tools:
        tools_clone = tools.copy()
        last_tool = tools_clone[-1].copy()
        last_tool["cache_control"] = {"type": "ephemeral"} # using this cache_control setting, we cache the tool calls.
        tools_clone[-1] = last_tool
        params["tools"] = tools_clone

    if system:
        params["system"] = [
            {
                "type": "text",
                "text": system,
                "cache_control": {"type": "ephemeral"}, # here cache system prompt.
            }
        ]

    response = client.messages.create(**params)

    usage = response.usage
    print("\n=== CACHE DEBUG ===")
    print("Cache Write:", getattr(usage, "cache_creation_input_tokens", 0))
    print("Cache Read :", getattr(usage, "cache_read_input_tokens", 0))
    print("===================\n")

    return response

def get_text(response):
    return "\n".join([block.text for block in response.content if block.type == "text"])

print("\n🔥 FIRST CALL (Expect CACHE MISS)\n")

messages1 = [
    {"role": "user", "content": "Analyze this chat: I love this product!"}
]

res1 = chat(messages1, system=SYSTEM_PROMPT, tools=tools)
print(get_text(res1))


print("\n🔥 SECOND CALL (Expect CACHE HIT)\n")

messages2 = [
    {"role": "user", "content": "Analyze this chat: This is terrible service."}
]

res2 = chat(messages2, system=SYSTEM_PROMPT, tools=tools)
print(get_text(res2))


print("\n🔥 THIRD CALL (BREAK CACHE)\n")

# ❌ small change breaks cache
modified_prompt = SYSTEM_PROMPT + " "

res3 = chat(messages2, system=modified_prompt, tools=tools)
print(get_text(res3))