// Hoisting → JS moves declarations to top of scope

// ========================================
// Key Idea:
// - Variables & functions are moved to top
// - Works in global & local scope
// ========================================

// ========================================
// Example 1: Variable Hoisting (var)
// ========================================

x = 10;
console.log(x); // 10

var x;

// JS treats it like:
// var x;
// x = 10;

// ========================================
// Example 2: Function Hoisting
// ========================================

sayHello(); // works

function sayHello() {
  console.log("Hello");
}

// ========================================
// Example 3: Local Scope Hoisting
// ========================================

function test() {
  y = 20;
  console.log(y); // 20

  var y;
}

test();

// ========================================
// Important Note
// ========================================

// Only declaration is hoisted, NOT value

var a;
console.log(a); // undefined
a = 5;

// ========================================
// let & const (is Hoisting but TDZ)
// ========================================

// console.log(b); ❌ error
let b = 10;

// console.log(c); ❌ error
const c = 20;

// ========================================
// Strict Mode
// ========================================

("use strict");

// d = 30; ❌ error (must declare first)
var d;

// ========================================
// INTERVIEW POINTS
// ========================================

/*
Hoisting:
- Moves declarations to top
- var → hoisted with undefined
- function → fully hoisted
- let/const → hoisted but in TDZ

Important:
- Only declaration hoisted, not initialization
*/

// ========================================
// Memory Tip 🧠
// ========================================

// "Hoisting = move declaration to top"
