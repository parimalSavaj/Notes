# 🧠 Claude API Response Architecture (v2.0)

When Claude responds to a request, it returns a structured JSON object. Your application logic must branch based on specific keys to handle text generation, tool execution, safety refusals, and token billing.

## 1. `stop_reason` (Traffic Control)

This key dictates how your backend processes the `content` array.

- **`"end_turn"`**: Success. Claude finished generating naturally.
- **`"tool_use"`**: Action Required. Claude is requesting a function call. Stop and execute the function identified in the `content` blocks.
- **`"max_tokens"`**: Limit reached. Generation was cut off by your `max_tokens` setting.
- **`"stop_sequence"`**: Triggered. The model hit a custom string you defined.
- **`"refusal"`**: Safety trigger. The model declined the request due to policy violations. **Check `stop_details` for the reason.**

## 2. `content` Array (Polymorphic Payload)

Claude returns an array of objects. **Always inspect the `type` property.** Do not assume index `0` is always a final text answer.

| Type             | Action                 | Key to Read                  |
| ---------------- | ---------------------- | ---------------------------- |
| **`"text"`**     | Display to user        | `block.text`                 |
| **`"tool_use"`** | Execute local function | `block.name` & `block.input` |
| **`"thinking"`** | Log/UI Debugging       | `block.thinking`             |

- **Pro Tip:** If a response contains multiple blocks (e.g., a `thinking` block followed by a `text` block), ensure your UI only displays the `text` as the "answer" to keep the experience clean.

## 3. `usage` (Billing & Context Management)

Use these keys to manage your context window and track API costs.

- **`input_tokens`**: The total cost for your prompt + history.
- **`output_tokens`**: The cost for Claude's generated answer.
- **`cache_read_input_tokens`**: Tokens successfully pulled from your Prompt Cache (Cheaper).
- **`cache_creation_input_tokens`**: Tokens newly written to your Prompt Cache (Expensive).

## 4. `stop_details` (Safety & Guardrails)

Available when `stop_reason` is `"refusal"`.

- **`type`**: Usually `"refusal"`.
- **`reason`**: The policy category that triggered the block (e.g., `"policy_violation"`, `"cyber"`, `"bio"`). Use this to inform the user or log for compliance.

---

## 💻 Example: Advanced API Response Object

```json
{
  "id": "msg_01...",
  "role": "assistant",
  "model": "claude-fable-5",
  "stop_reason": "tool_use",
  "content": [
    {
      "type": "thinking",
      "thinking": "The user wants sales data for Q3. I should use the get_sales tool."
    },
    {
      "type": "tool_use",
      "id": "toolu_01...",
      "name": "get_sales_data",
      "input": { "quarter": "Q3" }
    }
  ],
  "usage": {
    "input_tokens": 500,
    "cache_read_input_tokens": 400,
    "cache_creation_input_tokens": 0,
    "output_tokens": 80
  }
}
```

---

## 📝 The Golden Rules for Your Code

1. **Iterate, Don't Guess**: Use a loop or `.find()` to search for `tool_use` types before rendering text.
2. **Safety First**: Always handle `stop_reason: "refusal"` before parsing `content`. If it’s a refusal, the content may be empty or incomplete.
3. **Cache Awareness**: If `cache_read_input_tokens` is consistently `0`, your cache breakpoints are likely in the wrong place. Review your `cache_control` strategy.
4. **Looping Logic**: If `stop_reason === "tool_use"`, execute the tool, append the result as a `tool_result` content block, and send it back to the API to continue the conversation.
