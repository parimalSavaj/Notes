// Recursion → function calling itself

// ========================================
// Key Idea
// ========================================

// - Function repeats itself
// - Must have a BASE CONDITION (stop)

// ========================================
// Example 1: Sum of numbers
// ========================================

function add(n) {
  if (n <= 0) return 0; // base condition

  return n + add(n - 1);
}

console.log(add(3)); // 6

// Flow:
// add(3) → 3 + add(2)
//        → 3 + 2 + add(1)
//        → 3 + 2 + 1 + add(0)
//        → 6

// ========================================
// Example 2: Sum of array
// ========================================

function computeSum(arr) {
  if (arr.length === 1) return arr[0]; // base

  return arr.pop() + computeSum(arr);
}

console.log(computeSum([7, 8, 9, 99])); // 123

// ========================================
// Important Points
// ========================================

/*
Recursion:
- Function calls itself
- Needs base condition to stop
- Without base → infinite loop

Use cases:
- Trees, graphs
- Factorial, sum, search
*/
