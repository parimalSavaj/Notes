// Data Types in JavaScript
// Use typeof to check type

// ========================================
// 1. Primitive Data Types
// (Store single value)
// ========================================

// String → text (use '' or "")
let str1 = "John";
let str2 = "Doe";

// Number → integer or decimal
let num1 = 10;
let num2 = 3.14;

// BigInt → very large numbers (add 'n')
let big = 123456789012345678901234567890n;

// Boolean → true / false
let isTrue = true;

// Undefined → declared but no value
let x;
console.log(x); // undefined

// Null → empty / no value
let y = null;

// Symbol → unique value (ES6)
let sym = Symbol("id");

// ========================================
// typeof examples
// ========================================

console.log(typeof "abc"); // string
console.log(typeof 10); // number
console.log(typeof true); // boolean
console.log(typeof 10n); // bigint
console.log(typeof undefined); // undefined
console.log(typeof null); // object (JS bug)
console.log(typeof Symbol()); // symbol

// ========================================
// 2. Non-Primitive Data Types
// (Store multiple / complex values)
// ========================================

// Object → key-value pairs
let obj = {
  name: "John",
  age: 25,
  greet: function () {
    return this.name;
  },
};

// Array → ordered list
let arr = [1, "hello", true];

// ========================================
// INTERVIEW POINTS
// ========================================

/*
Primitive:
- string, number, bigint, boolean, undefined, null, symbol

Non-Primitive:
- object, array, function

Key Notes:
- typeof null → "object" (bug)
- Primitive → single value
- Non-primitive → multiple values
*/
