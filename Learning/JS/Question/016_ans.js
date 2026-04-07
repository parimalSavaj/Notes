// map(), filter(), reduce() → array methods

// ========================================
// map() → transform each element
// ========================================

const nums = [1, 2, 3];

const doubled = nums.map((n) => n * 2);

console.log(doubled); // [2, 4, 6]

// - returns new array
// - original array unchanged

// ========================================
// filter() → select elements
// ========================================

const numbers = [1, 2, 3, 4];

const even = numbers.filter((n) => n % 2 === 0);

console.log(even); // [2, 4]

// - returns filtered array
// - keeps only matching values

// ========================================
// reduce() → single value
// ========================================

const arr = [1, 2, 3, 4];

const sum = arr.reduce((acc, n) => acc + n, 0);

console.log(sum); // 10

// acc → accumulator (result)
// 0 → initial value

// ========================================
// Important Note
// ========================================

// Missing initial value can cause issues
// especially for empty arrays

// ========================================
// Chaining Example
// ========================================

const users = [
  { name: "Rahul", isActive: true },
  { name: "Amit", isActive: true },
  { name: "John", isActive: false },
];

const result = users
  .filter((u) => u.isActive)
  .map((u) => u.name)
  .reduce((acc, name) => acc + ", " + name, "");

console.log(result); // ", Rahul, Amit"

// ========================================
// map vs forEach
// ========================================

/*
map:
- returns new array

forEach:
- returns undefined
- use for side effects
*/

// ========================================
// INTERVIEW POINTS
// ========================================

/*
map → transform
filter → select
reduce → single value

All:
- return new result
- do not modify original array
*/
