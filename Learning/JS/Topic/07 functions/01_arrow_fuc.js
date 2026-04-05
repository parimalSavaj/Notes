// ===================== ARROW FUNCTIONS (Lambda expressions) =====================

/*
 Arrow functions = shorter way to write functions in JavaScript

 Introduced in ES6

 Best for:
 - Small functions
 - Callbacks (map, filter, etc.)
 - Simple logic
*/

// ===================== BASIC SYNTAX =====================

// Multiple parameters
const add = (a, b) => a + b;

// Single parameter (no brackets needed)
const square = (x) => x * x;

// No parameters
const greet = () => console.log("Hello");

// Multiple lines (must use return)
const multiplyAndDouble = (a, b) => {
  const result = a * b;
  return result * 2;
};

// ===================== RETURN RULES =====================

/*
 1. Single line → auto return (no "return" needed)
 2. Multiple lines → must use "return"
*/

const sum = (a, b) => a + b; // auto return

const sum2 = (a, b) => {
  return a + b; // required
};

// ===================== RETURN OBJECT =====================

/*
 To return object → wrap in ()
 Otherwise {} is treated as function body
*/

const getUser = () => ({ name: "John", age: 30 });

// ===================== "this" BEHAVIOR =====================

/*
 Arrow functions DO NOT have their own "this"
 They take "this" from their parent (lexical scope)
*/

const user = {
  name: "Rahul",
  normalFunc: function () {
    console.log("Normal:", this.name); // works
  },
  arrowFunc: () => {
    console.log("Arrow:", this.name); // undefined (wrong)
  },
};

user.normalFunc();
user.arrowFunc();

// ===================== WHEN TO USE =====================

/*
 ✔ Use Arrow Functions:
 - Callbacks (map, filter, reduce)
 - Short/simple functions
 - When you need parent "this"
*/

// ===================== WHEN NOT TO USE =====================

/*
 ❌ Avoid Arrow Functions:
 - Object methods
 - Constructors (cannot use "new")
 - Event handlers (sometimes confusing "this")
*/

// ===================== CONSTRUCTOR LIMITATION =====================

/*
 Arrow functions cannot be used as constructor
*/

const Person = (name) => {
  this.name = name;
};

// const p = new Person("John"); ❌ Error

// ===================== NO "arguments" OBJECT =====================

/*
 Arrow functions don't have "arguments"
 Use rest operator instead
*/

const test = (...args) => {
  console.log(args);
};

// ===================== CALLBACK EXAMPLES =====================

const numbers = [1, 2, 3, 4];

// Traditional
const doubled1 = numbers.map(function (n) {
  return n * 2;
});

// Arrow function (clean)
const doubled2 = numbers.map((n) => n * 2);

// ===================== QUICK COMPARISON =====================

/*
Feature            | Normal Function     | Arrow Function
------------------ | ------------------- | -------------------
Syntax             | Longer             | Shorter
this               | Own                | Inherited (parent)
arguments          | Available          | Not available
Constructor        | Yes                | No
Best Use           | Methods            | Callbacks
*/

// ===================== MEMORY TRICKS =====================

/*
 arrow (=>) = short function

 call/apply/bind not needed often
 because arrow keeps parent "this"

 Use arrow → when simple & clean code needed
*/
