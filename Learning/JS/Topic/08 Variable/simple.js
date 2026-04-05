/*
========================================
JavaScript var, let, const (Quick Notes)
========================================

SCOPE:
- Function scope → inside function
- Block scope {} → inside if, for, etc.

----------------------------------------
var (Avoid using)
----------------------------------------
- Scope → Function (ignores {})
- Redeclare → Yes
- Reassign → Yes
- Hoisting → Yes (value = undefined)

Example:
*/
var x = 10;
var x = 20; // allowed

if (true) {
  var a = 5;
}
console.log(a); // works (no block scope)

console.log(b); // undefined ( hoisting )
var b = 10;

/*
----------------------------------------
let (Use when value changes)
----------------------------------------
- Scope → Block {}
- Redeclare → No
- Reassign → Yes
- Hoisting → Yes but TDZ (error before declare)

Example:
*/
let y = 10;
y = 20; // ok

// let y = 30; ❌ error

if (true) {
  let c = 5;
}
// console.log(c); ❌ error

// console.log(d); ❌ error
let d = 10;

/*
----------------------------------------
const (Default choice)
----------------------------------------
- Scope → Block {}
- Redeclare → No
- Reassign → No
- Must initialize → Yes
- Hoisting → TDZ

Example:
*/
const z = 10;
// z = 20; ❌ error

/*
Important (Objects & Arrays):
- Cannot reassign
- Can modify inside
*/
const user = { name: "A" };
user.name = "B"; // ✅ allowed

const arr = [1];
arr.push(2); // ✅ allowed

/*
----------------------------------------
INTERVIEW POINTS:
----------------------------------------
- var → function scoped
- let/const → block scoped
- var allows redeclare, others don’t
- const must be initialized
- let/const have TDZ
- const objects/arrays mutable inside

*/
