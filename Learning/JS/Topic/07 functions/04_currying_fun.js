// Currying → convert function with multiple args
// into multiple functions with single arg

// ========================================
// Basic Example
// ========================================

function add(a) {
  return function (b) {
    return a + b;
  };
}

console.log(add(3)(4)); // 7

// Normal → add(a, b)
// Curried → add(a)(b)

// ========================================
// Why use Currying?
// ========================================

// - Reuse functions
// - Fix some arguments early
// - Cleaner & modular code

// ========================================
// Convert normal function to curried
// ========================================

function multiply(a, b) {
  return a * b;
}

function curry(fn) {
  return function (a) {
    return function (b) {
      return fn(a, b);
    };
  };
}

const curriedMultiply = curry(multiply);

console.log(multiply(4, 3)); // 12
console.log(curriedMultiply(4)(3)); // 12

// ========================================
// Real Use Case
// ========================================

const multiplyBy2 = curriedMultiply(2);

console.log(multiplyBy2(5)); // 10
console.log(multiplyBy2(10)); // 20

// ========================================
// INTERVIEW POINTS
// ========================================

/*
Currying:
- Breaks function into smaller functions
- Each function takes one argument
- Does not change result, only how it's called

Example:
f(a, b) → f(a)(b)
*/
