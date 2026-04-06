// map() vs forEach()

// ========================================
// forEach() → just loop (no return)
// ========================================

const arr = [1, 2, 3];

arr.forEach((num) => {
  console.log(num * 2);
});

// Output: 2, 4, 6
// ❌ No new array returned

// ========================================
// map() → transform & return new array
// ========================================

const result = arr.map((num) => {
  return num * 2;
});

console.log(result); // [2, 4, 6]

// ========================================
// Key Differences
// ========================================

/*
forEach:
- Just loops
- No return (undefined)
- Used for side effects (log, update)

map:
- Transforms data
- Returns new array
- Can chain (map().filter())
*/

// ========================================
// Common Mistake
// ========================================

// ❌ Wrong use of map
arr.map((num) => {
  console.log(num);
});

// Should use forEach instead

// ========================================
// Chaining (only map)
// ========================================

const output = arr.map((n) => n * 2).filter((n) => n > 2);

console.log(output); // [4, 6]
