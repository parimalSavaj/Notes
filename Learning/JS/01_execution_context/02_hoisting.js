// Hoisting is JavaScript's behavior where declarations are processed
// during the Memory Creation Phase of the Execution Context,
// before the code is executed.

// It does NOT mean code is physically moved.
// Instead, JavaScript allocates memory for variables and functions in advance.

// Hoisting happens inside the Memory Creation Phase
// of the Global Execution Context (and also in function execution contexts).

/*
| Type       | Hoisted? | Initialized?        |
| ---------- | -------- | ------------------- |
| var        | ✅ Yes    | undefined           |
| let        | ✅ Yes    | ❌ (TDZ - uninitialized) |
| const      | ✅ Yes    | ❌ (TDZ - uninitialized) |
| function   | ✅ Yes    | ✅ Fully initialized |
*/

// Example 1:
console.log(a);
var a = 5;

// Output:
// undefined

// Example 2:
greet();

function greet() {
  console.log("Hi");
}

// Output:
// Hi

// Example 3:
// console.log(b);
// let b = 10;

// Output:
// ReferenceError (because of Temporal Dead Zone)

// Key Point:
// Hoisting does not move values, only declarations are registered in memory.

// Ans:
// “Hoisting is the behavior where JavaScript processes variable and function declarations during the memory creation phase of the execution context. Variables declared with var are initialized with undefined, while let and const remain uninitialized in the Temporal Dead Zone. Function declarations are fully hoisted with their definitions.”
