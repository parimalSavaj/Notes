# Prompt Evaluation (Cheat Sheet)

**Why do this?**
To prove a new prompt or model is actually better using data, not just "vibes," and to make sure fixing one thing didn't silently break something else.

### The 3-Step Flow

**1. Eval Dataset (The Test Cases)**

- **What it is:** A list of test inputs and expected outputs, usually stored in JSON.
- **How to make it:** Use a fast/cheap LLM to generate synthetic test cases based on your context.
- **Format:** `{"task": "user input", "solution_criteria": "what a perfect answer looks like"}`

**2. Production Model (The Test Run)**

- **What it is:** The actual execution step.
- **How to do it:** Feed the `task` from your dataset into your _new_ prompt using your main LLM. Capture the raw output.

**3. The Grader (The Scoring)**
Evaluate the captured output against the `solution_criteria` using three methods:

- **Code-Based:** Scripts check for strict rules (e.g., Does it parse as valid JSON? Does the generated code compile?).
- **Model-Based (LLM-as-a-Judge):** A smart model (like GPT-4o) reads the output and the criteria, and gives it a Pass/Fail or a score (1-5).
- **Human Check:** A person manually reviews a small random sample (5%) to ensure the automated graders aren't making mistakes.
