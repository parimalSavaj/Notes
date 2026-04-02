# How async / await Actually Works

`async/await` is syntactic sugar over Promises. It makes asynchronous code look and behave like synchronous code, making it easier to read.

## The `async` Keyword

- Putting `async` in front of a function guarantees that the function will always return a **Promise**.
- If you return a regular value (like `return 5`), JavaScript automatically wraps it in a resolved Promise (`Promise.resolve(5)`).

## The `await` Keyword (The Pause Button)

- `await` can only be used inside an `async` function.
- When the engine hits an `await` statement:
  1. It hands the asynchronous task (like a `fetch` request) to the Web APIs.
  2. It **suspends** the execution of that specific `async` function and pops it off the Call Stack.
  3. The function immediately returns a **pending Promise** to whatever called it.
  4. The JavaScript engine goes back to the global execution context and continues running any synchronous code outside the function.

## Resuming the Function

- When the awaited background task finishes, the Web API takes the **remainder** of the `async` function (everything below the `await` line) and pushes it into the **Microtask Queue**.
- Once the Call Stack is empty, the Event Loop pushes that remaining code back onto the stack to finish executing.

## The Pending Promise Gotcha

If you call an `async` function and assign it to a variable without awaiting it on the outside, you will get a pending Promise, not the actual data:

```javascript
async function getData() {
  const ans = await fetch(
    "[https://api.example.com/data](https://api.example.com/data)",
  );
  return ans;
}

// This runs immediately while getData is paused, so it prints a Pending Promise!
const ans = getData();
console.log(ans);
```
