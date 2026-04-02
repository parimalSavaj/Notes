# JavaScript Concurrency Model: Event Loop & Queues

JavaScript is single-threaded, meaning it can only execute one piece of code at a time in the **Call Stack**. However, it handles asynchronous operations without blocking the main thread using the Event Loop and Web APIs.

## 1. The Call Stack (The Execution Area)

- Executes synchronous code line by line.
- If it encounters a time-consuming asynchronous task (like `setTimeout`, `fetch`, or DOM events), it does not wait. It hands the task off to the Web APIs and immediately moves to the next line of code.

## 2. Web APIs (The Background Workers)

- Provided by the browser (or Node.js environment), not the JavaScript engine itself.
- Handles timers, network requests, and events in the background.
- When a background task finishes, the Web API pushes the **callback function** into one of two queues.

## 3. The Queues (The Waiting Area)

- **Microtask Queue (High Priority):** Holds Promises (`.then()`, `.catch()`) and the remainder of `async/await` functions.
- **Macrotask Queue (Low Priority):** Holds `setTimeout`, `setInterval`, and DOM event callbacks.

## 4. The Event Loop (The Traffic Controller)

- Constantly monitors the Call Stack.
- **Rule 1:** It only acts when the Call Stack is completely empty.
- **Rule 2:** It will completely drain the **Microtask Queue** first. If a microtask creates another microtask, it executes that immediately.
- **Rule 3:** Once the Microtask Queue is 100% empty, it will take one task from the **Macrotask Queue** and push it to the Call Stack.
