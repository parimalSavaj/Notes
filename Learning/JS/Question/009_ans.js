// Objects comparison → compares reference, NOT values

// ========================================
// Example 1: Same content, different objects
// ========================================

const a = { name: "Ankit" };
const b = { name: "Ankit" };

console.log(a === b); // false

// Reason:
// - Different memory location

// ========================================
// Example 2: Same reference
// ========================================

const x = { name: "Ankit" };
const y = x;

console.log(x === y); // true

// Reason:
// - Both point to same object

// ========================================
// Key Rule
// ========================================

// Objects are equal ONLY if reference is same

// ========================================
// Compare values (quick trick)
// ========================================

const obj1 = { name: "A" };
const obj2 = { name: "A" };

console.log(JSON.stringify(obj1) === JSON.stringify(obj2)); // true

// ========================================
// Limitations of stringify
// ========================================

/*
- Depends on key order
- Ignores functions, undefined
- Fails for circular objects
*/

// ========================================
// INTERVIEW POINTS
// ========================================

/*
- == and === behave same for objects
- Compare reference, not content
- Same object → true
- Different objects → false (even if same data)
- Deep compare needs custom function or library
*/
