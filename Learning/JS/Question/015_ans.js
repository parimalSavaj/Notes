// async / await → cleaner way to handle Promises

// ========================================
// async → always returns Promise
// ========================================

async function getValue() {
  return 10;
}

console.log(getValue()); // Promise {10}

// ========================================
// await → wait for Promise result
// ========================================

async function getData() {
  const res = await fetch("https://jsonplaceholder.typicode.com/users");
  const data = await res.json();

  console.log(data);
}

// Note:
// - pauses function (not whole JS)
// - only works inside async

// ========================================
// Error Handling (try...catch)
// ========================================

async function getUsers() {
  try {
    const res = await fetch("https://jsonplaceholder.typicode.com/users");
    const data = await res.json();

    console.log(data);
  } catch (err) {
    console.log("Error:", err);
  }
}

// Same as .then().catch()

// ========================================
// Common Mistakes
// ========================================

/*
1. Missing await → returns pending promise
2. await inside forEach ❌ (doesn't wait)
*/

// ========================================
// Sequential vs Parallel
// ========================================

// Sequential (slow)
for (const user of users) {
  await fetch(user.url);
}

// Parallel (fast)
const promises = users.map((u) => fetch(u.url));
await Promise.all(promises);

// ========================================
// Promise.all vs allSettled
// ========================================

// Promise.all → fails if one fails
await Promise.all(promises);

// Promise.allSettled → gives all results
await Promise.allSettled(promises);

// ========================================
// INTERVIEW POINTS
// ========================================

/*
async:
- returns Promise

await:
- waits for result
- only inside async

Error:
- use try...catch

Parallel:
- Promise.all (fast)
- allSettled (safe)
*/
