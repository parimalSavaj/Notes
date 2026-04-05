/*
========================================
IIFE (Immediately Invoked Function Expression)
========================================

Definition:
- A function that runs immediately after it is created.

Syntax:
*/
(function () {
  // code here
})();

/*
Why use IIFE?
- To create private variables (data privacy)
- Variables inside cannot be accessed outside

Example:
*/
(function () {
  var message = "IIFE";
  console.log(message); // works inside
})();

/*
Outside access:
*/
console.log(message); // ❌ Error: not defined

/*
INTERVIEW POINTS:
- Runs immediately
- Creates private scope
- Avoids global variable pollution

MEMORY TIP:
IIFE = "Run instantly + keep data private"
*/
