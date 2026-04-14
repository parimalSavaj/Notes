> Q. Browser and Node.js both run JavaScript, but they serve different purposes.

The browser is used for the frontend and user interaction, while Node.js is used for backend tasks like servers, file handling, and APIs.
The browser gives access to window and document, while Node.js gives access to the file system, process, and server-related features.

---

## Node.js Runtime Environment vs Browser (Simple Answer)

- A **runtime environment** is where JavaScript code runs.

### Browser

- Runs JavaScript inside web browsers like Chrome or Firefox
- Used for **frontend (user interface)**
- Can interact with web pages (HTML, CSS)
- Provides objects like `window` and `document`
- Does **not** allow direct access to system files for security

### Node.js

- Runs JavaScript outside the browser
- Used for **backend (server-side work)**
- Can handle servers, APIs, and file operations
- Does **not** have `window` or `document`
- Allows access to system resources like files and processes

### Key Difference

- **Browser → frontend, UI-focused, limited system access**
- **Node.js → backend, server-focused, full system access**
