# Quick Reference: LLM Tool Calling

**What it is:** Giving an LLM the ability to interact with the outside world by pausing its text generation, asking your code to run a function, and using the result to construct the final answer.

## The 5-Step Execution Loop

1. **Define the Function:** Write the actual code function in your backend (e.g., `add_hours(time, hours)`).
2. **Create the Schema:** Write a JSON description of your function so the LLM knows it exists and how to use it.
3. **First LLM Call (The Decision):** Send the user's message + the JSON schema to the LLM. Instead of answering with text, the LLM replies: _"Call this tool with these arguments."_
4. **Execute the Code:** Your app catches this request, runs your actual backend function, and gets a concrete result.
5. **Second LLM Call (The Answer):** Send the original message + the tool execution result back to the LLM. The LLM reads your result and generates a natural, human-friendly response.

---

## JSON Schema Template Example

```json
[
  {
    "type": "function",
    "function": {
      "name": "add_hours",
      "description": "Add a specific number of hours to a given time.",
      "parameters": {
        "type": "object",
        "properties": {
          "current_time": {
            "type": "string",
            "description": "The starting time to add hours to."
          },
          "hours": {
            "type": "integer",
            "description": "The number of hours to add."
          }
        },
        "required": ["current_time", "hours"]
      }
    }
  }
]
```

## Key Schema Rules

- **`name`:** Must exactly match the function name in your code.
- **`description`:** This is the most critical field. The LLM reads this text to figure out _when_ it should trigger the tool.
- **`properties`:** The arguments (strings, integers, etc.) your function expects.
- **`required`:** The specific arguments the LLM absolutely must provide so your code doesn't crash.
