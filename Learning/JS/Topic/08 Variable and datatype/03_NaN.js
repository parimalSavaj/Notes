// NaN → "Not-a-Number"
// Represents invalid number

// ========================================
// Basic Example
// ========================================

let x = "hello" / 2;
console.log(x); // NaN

// ========================================
// Type of NaN
// ========================================

console.log(typeof NaN); // "number" (important interview point)

// ========================================
// isNaN() → check if value is NaN
// ========================================

console.log(isNaN("Hello")); // true
console.log(isNaN(345)); // false
console.log(isNaN("1")); // false (converted to number)
console.log(isNaN(true)); // false (true → 1)
console.log(isNaN(false)); // false (false → 0)
console.log(isNaN(undefined)); // true

// ========================================
// Important Note
// ========================================

// isNaN() converts value to number first
// then checks if it is NaN

// ========================================
// INTERVIEW POINTS
// ========================================

/*
NaN:
- Means invalid number
- typeof NaN → "number"
- isNaN() checks NaN after conversion

Tricky:
- "1", true, false → NOT NaN
- undefined → NaN
*/

// ========================================
// Memory Tip 🧠
// ========================================

// "NaN = not a valid number"
