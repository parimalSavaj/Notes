// Rest (...) & Spread (...) → ES6 features

// ========================================
// Rest Parameter → collect values into array
// ========================================

// Used in function parameters

function getArgs(...args) {
  console.log(args); // array
}

getArgs(1, 2, 3); // [1, 2, 3]

// Example: sum all values
function sum(...nums) {
  return nums.reduce((acc, val) => acc + val, 0);
}

console.log(sum(1, 2, 3, 4)); // 10

// Must be last parameter
// function test(a, ...b, c) ❌ error
function test(a, ...b) {} // ✅

// ========================================
// Spread Operator → expand values
// ========================================

// Used in function call / arrays / objects

// Example: function call
function add(a, b, c, d) {
  return a + b + c + d;
}

const arr = [1, 2, 3, 4];
console.log(add(...arr)); // 10

// ========================================
// Array usage
// ========================================

const arr1 = [1, 2];
const arr2 = [...arr1]; // clone
console.log(arr2); // [1, 2]

// ========================================
// Object usage
// ========================================

const obj1 = { x: 1, y: 2 };
const obj2 = { z: 3 };

const merged = { ...obj1, ...obj2 };
console.log(merged); // {x:1, y:2, z:3}

// ========================================
// INTERVIEW POINTS
// ========================================

/*
Rest:
- Collect arguments into array
- Used in function parameters
- Must be last

Spread:
- Expands array/object
- Used in function calls, cloning, merging

Key Difference:
- Rest → gather values
- Spread → spread values
*/
