// Promise → handles async operations (future result)

// States:
// - pending → waiting
// - fulfilled → success
// - rejected → error

// ========================================
// Basic Example
// ========================================

const promise = new Promise((resolve, reject) => {
  let success = true;

  if (success) {
    resolve("Data received"); // success
  } else {
    reject("Error occurred"); // failure
  }
});

// Handle result
promise
  .then((res) => {
    console.log(res); // success
  })
  .catch((err) => {
    console.log(err); // error
  });

// ========================================
// Why use Promises?
// - Handle async tasks (API, DB, setTimeout)
// - Avoid callback hell
// ========================================

// ========================================
// Real Example (setTimeout)
// ========================================

function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Data loaded");
    }, 1000);
  });
}

fetchData()
  .then((data) => console.log(data))
  .catch((err) => console.log(err));

// ========================================
// Chaining Promises
// ========================================

Promise.resolve(10)
  .then((num) => num * 2)
  .then((num) => num + 5)
  .then((result) => console.log(result)); // 25

// ========================================
// INTERVIEW POINTS
// ========================================

/*
Promise:
- Object for async result
- Has 3 states → pending, fulfilled, rejected
- Uses .then() for success
- Uses .catch() for error
- Supports chaining

Methods:
- resolve() → success
- reject() → failure
*/

// ========================================
// Memory Tip 🧠
// ========================================

// "Promise = future value (success or error)"
