// Higher Order Function (HOF)
// → Function that uses another function
// (takes function as argument OR returns function)

// ========================================
// Example 1: Function as argument
// ========================================

function higherOrder(fn) {
  fn();
}

higherOrder(function () {
  console.log("Hello");
});

// ========================================
// Example 2: Function returning function
// ========================================

function higherOrder2() {
  return function () {
    return "Do something";
  };
}

const result = higherOrder2();
console.log(result()); // "Do something"

// ========================================
// Why possible?
// ========================================

// Functions are "first-class citizens"
// → can store, pass, return like variables

// ========================================
// Real Examples (Built-in HOF)
// ========================================

const arr = [1, 2, 3];

arr.map((num) => num * 2); // returns new array
arr.filter((num) => num > 1); // filters values
arr.forEach((num) => console.log(num)); // loop

// ========================================
// INTERVIEW POINTS
// ========================================

/*
HOF:
- Takes function as argument
- OR returns a function

Because:
- Functions are first-class citizens

Examples:
- map, filter, forEach
*/

// ========================================
// Memory Tip 🧠
// ========================================

// "HOF = function using another function"
