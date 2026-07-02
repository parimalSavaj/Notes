from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic
from datetime import datetime, timedelta


client = Anthropic()

def get_time():
    return datetime.now().strftime("%H:%M:%S")

def add_hours(time_str, hours):
    time_obj = datetime.strptime(time_str, "%H:%M:%S")
    return (time_obj + timedelta(hours=hours)).strftime("%H:%M:%S")

tools = [
    {
        "name": "get_time",
        "description": "Get current time",
        "input_schema": {"type": "object", "properties": {}}
    },
    {
        "name": "add_hours",
        "description": "Add hours to time",
        "input_schema": {
            "type": "object",
            "properties": {
                "time_str": {"type": "string"},
                "hours": {"type": "integer"}
            },
            "required": ["time_str", "hours"]
        }
    }
]

messages = [
    {"role": "user", "content": "What is current time and time after 2 hours?"}
]

while True:
    response = client.messages.create(
        model="claude-sonnet-4-0",
        messages=messages,
        tools=tools,
        max_tokens=200
    )

    # ✅ ADD THIS: store Claude's response
    messages.append({
        "role": "assistant",
        "content": response.content
    })

    stop = True  # assume no more tools

    for block in response.content:
        if block.type == "tool_use":
            stop = False

            if block.name == "get_time":
                result = get_time()
                print("Current Time:", result)

            elif block.name == "add_hours":
                result = add_hours(result, 2)
                print("After 2 Hours:", result)

            # send result back
            messages.append({
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                }]
            })

    if stop:
        break