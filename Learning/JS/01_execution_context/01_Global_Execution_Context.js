// The Global Execution Context (GEC) is the default execution environment
// where JavaScript code starts running.

// The Global Execution Context has 2 phases:
// 1. Memory Creation Phase
// 2. Execution Phase

// 1. Memory Creation Phase:
// - JavaScript allocates memory for variables and functions
// - Variables declared with var are initialized with 'undefined'
// - What about let and const we see inside hoisting and TDZ
// - Function declarations are stored with their full definition

// 2. Execution Phase:
// - Code is executed line by line
// - Variables are assigned actual values
// - Functions are invoked when called

// Example:

var a = 10;

function foo() {
  console.log("Hello");
}

console.log(a);

// Memory Phase:
// a → undefined
// foo → function definition

// Execution Phase:
// a → 10
// console.log(a) → 10

// Ans:
// Global Execution Context is created when JavaScript starts executing, and it has two phases: memory creation where variables are initialized and functions are stored, and execution phase where code runs line by line.
