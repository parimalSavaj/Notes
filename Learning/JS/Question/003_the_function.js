// ===================== FIRST-CLASS FUNCTIONS =====================

/*
 First-Class = JavaScript rule (capability)

 It means:
 Functions behave like normal variables

 You can:
 ✔ Store function in variable
 ✔ Pass function as argument
 ✔ Return function from another function
*/

const sayHello = function () {
  return "Hello!";
};

// ===================== FIRST-ORDER FUNCTION =====================

/*
 First-Order = simple/normal function

 It:
 ❌ Does NOT take function as argument
 ❌ Does NOT return a function
 ✔ Works with normal values (number, string, etc.)
*/

function multiply(a, b) {
  return a * b;
}

console.log(multiply(5, 2)); // 10

// ===================== HIGHER-ORDER FUNCTION =====================

/*
 Higher-Order = function that works with other functions

 It:
 ✔ Takes function as argument (callback)
 ✔ OR returns a function
*/

// ---------- Example 1: Takes function as argument ----------

function processData(data, callback) {
  return callback(data);
}

const makeUppercase = (text) => text.toUpperCase();

console.log(processData("hello", makeUppercase)); // HELLO

// ---------- Example 2: Returns a function ----------

function createMultiplier(multiplier) {
  return function (number) {
    return number * multiplier;
  };
}

const doubleIt = createMultiplier(2);

console.log(doubleIt(10)); // 20

// ===================== REAL CONNECTION =====================

/*
 bind() is also a Higher-Order Function
 because it RETURNS a new function
*/

// ===================== QUICK COMPARISON =====================

/*
Type            | Meaning
--------------- | -----------------------------------------
First-Class     | Functions behave like variables
First-Order     | Normal function (no function input/output)
Higher-Order    | Works with functions (input or output)
*/
