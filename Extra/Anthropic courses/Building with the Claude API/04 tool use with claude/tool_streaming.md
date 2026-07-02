### Handling LLM Tool Calling Streams

**The Core Problem** LLMs stream tool arguments as broken, incomplete JSON chunks (e.g., `{"search_` or `query": "d`). If a frontend tries to parse this live using `JSON.parse()`, the application will crash.

To fix this, you have three architectural choices:

---

#### 1. The Buffered Gatekeeper (Wait, Validate, Render)

- **How it works:** The frontend ignores the live stream and shows a "Loading..." state. It waits until the LLM finishes writing, runs a standard `try/catch` on the final JSON, and then renders the data (or an error).
- **Pros:** Bulletproof UI stability. Zero layout shifts. No complex parsing libraries needed. Clean error handling.
- **Cons:** The user has to wait a few seconds before seeing the result.
- **When to use:** Best for small, fast tool calls (e.g., fetching a date, writing a quick SQL query, applying a filter).

#### 2. The Real-Time Streamer (Client-Side Parsing)

- **How it works:** The frontend uses a specialized "partial parser" (like `jsonrepair`) to artificially close broken brackets on every single incoming character. It feeds this partial data into the UI so the user sees fields typing out live.
- **Pros:** Feels incredibly fast and highly responsive.
- **Cons:** High engineering complexity. If the LLM hallucinates or cuts off mid-stream, you must implement "Last Known Good State" logic to freeze the UI and prevent a crash.
- **When to use:** Best for massive tool payloads (e.g., writing 500 lines of code into a JSON parameter, generating long articles).

#### 3. Generative UI (Server-Side Parsing / React Server Components)

- **How it works:** The broken JSON stream never touches the user's browser. It streams to your backend (e.g., Next.js server). The server pieces it together, renders the HTML/React components live, and streams the _finished UI_ to the frontend.
- **Pros:** The ultimate combination of speed and safety. Keeps parsing logic off the client device and keeps database credentials completely secure.
- **When to use:** The modern industry standard if you are building in Next.js using the Vercel AI SDK.

---

**💡 Golden Rule for AI Engineers:**
If the tool is just fetching data, hide it behind a loader (Option 1). If the tool _is_ the core product (like writing a long essay), stream it live (Option 2 or 3).
