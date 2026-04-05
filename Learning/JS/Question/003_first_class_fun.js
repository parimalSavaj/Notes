// ===================== FIRST-CLASS FUNCTIONS =====================

/*
 In JavaScript, functions are "first-class citizens"

 This means:
 Functions behave like normal variables
*/

// ===================== WHAT YOU CAN DO =====================

/*
 1. Store function in a variable
 2. Pass function as argument
 3. Return function from another function
*/

// ===================== 1. FUNCTION AS VARIABLE =====================

/*
 You can assign a function to a variable
*/

const greet = () => console.log("Hello");

greet(); // call the function

// ===================== 2. FUNCTION AS ARGUMENT =====================

/*
 You can pass a function into another function
 (called callback function)
*/

const sayHello = () => console.log("Hello!");

function execute(fn) {
  fn(); // call the passed function
}

execute(sayHello);

// Real example (browser event)

const handler = () => console.log("This is a click handler");

// Function passed as argument
document.addEventListener("click", handler);

// ===================== 3. FUNCTION AS RETURN VALUE =====================

/*
 A function can return another function
*/

function outer() {
  return function () {
    console.log("Inner function");
  };
}

const innerFunc = outer();
innerFunc();

// ===================== WHY IT'S IMPORTANT =====================

/*
 Because of this feature, JavaScript supports:

 ✔ Callbacks
 ✔ Higher-order functions
 ✔ Event handling
 ✔ Functional programming
*/

// ===================== QUICK SUMMARY =====================

/*
Feature                        | Example
----------------------------- | -------------------------
Store in variable             | const fn = () => {}
Pass as argument              | execute(fn)
Return from function          | return function() {}
*/
