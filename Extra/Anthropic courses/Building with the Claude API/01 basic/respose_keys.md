# 🧠 Claude API Response Architecture (AI Engineer Notes)

When Claude responds to a prompt, it returns a JSON object. Your backend code must read specific keys in this object to determine the next step in the agent logic.

## 1. `stop_reason` (Control Flow)

This key tells your code _why_ the LLM stopped generating output.

- **`"end_turn"`** 👉 **The conversation is done.** Claude has finished its final answer. Send the text to the user.
- **`"tool_use"`** 👉 **The conversation is paused.** Claude needs data. Your code must read the tool request, run the local function, and send the results back to Claude.
- **`"max_tokens"`** 👉 **Error state.** Claude hit the output length limit before finishing. Your code needs to handle a cut-off, incomplete string.
- **`"stop_sequence"`** 👉 **Rule triggered.** Claude generated a forbidden/custom stop word you defined, so the API halted it early.

## 2. `content` Array (Payload Parsing)

Because Claude can speak to the user and request a tool at the exact same time, the `content` is an array of objects. Your code loops through it and checks the `type` key:

- **`type: "text"`** 👉 Contains human-readable text (e.g., _"Let me check that..."_). Route this to the frontend UI.
- **`type: "tool_use"`** 👉 Contains computer instructions. Inside this block, you will find:
- `name`: The name of your function (e.g., `"get_sales_data"`)
- `input`: The JSON arguments for your function (e.g., `{"quarter": "Q3"}`)

## 3. `usage` (Memory & Billing Management)

This tracks the token count for the specific API call.

- **`input_tokens`** 👉 The size of the prompt and history you sent. Track this so you don't overflow the context window (memory limit). If this gets too high, trigger a function to summarize old messages.
- **`output_tokens`** 👉 The size of Claude's response. Track this to monitor your Anthropic API costs.

---

## 💻 Example API Response

```json
{
  "role": "assistant",
  "stop_reason": "tool_use",
  "content": [
    {
      "type": "text",
      "text": "Let me check the database for Q3."
    },
    {
      "type": "tool_use",
      "name": "get_sales_data",
      "input": { "quarter": "Q3" }
    }
  ],
  "usage": {
    "input_tokens": 450,
    "output_tokens": 65
  }
}
```

---

### 📖 API Rosetta Stone & SDK Abstraction

| Concept                     | Anthropic (Claude)    | OpenAI (GPT)                 | Google (Gemini)             | 🚀 Vercel AI SDK            |
| --------------------------- | --------------------- | ---------------------------- | --------------------------- | --------------------------- |
| **Stop Indicator Key**      | `stop_reason`         | `finish_reason`              | `finishReason`              | _Handled under the hood_    |
| **Value: "Done Talking"**   | `"end_turn"`          | `"stop"`                     | `"STOP"`                    | Stream resolves natively    |
| **Value: "Need a Tool"**    | `"tool_use"`          | `"tool_calls"`               | (Checks for `functionCall`) | Auto-triggers `execute()`   |
| **Value: "Limit Reached"**  | `"max_tokens"`        | `"length"`                   | `"MAX_TOKENS"`              | `finishReason === 'length'` |
| **Where is the text?**      | `content[].text`      | `choices[0].message.content` | `...parts[].text`           | `result.text`               |
| **Where is the tool JSON?** | `content[].tool_use`  | `...tool_calls[].function`   | `...parts[].functionCall`   | Parsed natively via Zod     |
| **Tokens (Memory In)**      | `usage.input_tokens`  | `usage.prompt_tokens`        | `...promptTokenCount`       | `usage.promptTokens`        |
| **Tokens (Memory Out)**     | `usage.output_tokens` | `usage.completion_tokens`    | `...candidatesTokenCount`   | `usage.completionTokens`    |

---

### 📝 Key Takeaway for Your Notes:

When you look at the first three columns, you are looking at the **Raw REST APIs**. If you build your app using those, you have to manually parse arrays, check specific strings, and write different `if/else` statements for every provider.

When you look at the **Vercel AI SDK column**, notice how there are almost no raw JSON paths. The SDK hides the complex API keys from you. It automatically finds the text, automatically validates the tool JSON, and automatically runs your backend functions regardless of which model is powering it.
