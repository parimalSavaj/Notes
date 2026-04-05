// Closure → function + its outer variables (even after outer function ends)

// ========================================
// Basic Example
// ========================================

function outer() {
  let count = 0; // local variable

  function inner() {
    count++;
    console.log(count);
  }

  return inner;
}

const counter = outer();

counter(); // 1
counter(); // 2
counter(); // 3

// ========================================
// Why it works?
// - inner() remembers variables of outer()
// - even after outer() is finished
// ========================================

// ========================================
// Real Use Case: Data Privacy
// ========================================

function createUser() {
  let password = "12345"; // private

  return {
    checkPassword: function (input) {
      return input === password;
    },
  };
}

const user = createUser();

console.log(user.checkPassword("12345")); // true
console.log(user.password); // ❌ undefined (private)

// ========================================
// Key Points
// ========================================

/*
Closure:
- Function remembers outer variables
- Keeps variables alive
- Used for data hiding

Use cases:
- Private data
- Counters
- Factory functions
*/

// ========================================
// Memory Tip 🧠
// ========================================

// "Closure = function + memory of parent variables"
