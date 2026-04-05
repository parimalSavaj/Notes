// Temporal Dead Zone (TDZ)

// The Temporal Dead Zone is the time between the start of a block scope
// and the point where a variable is declared and initialized.

// It applies to variables declared with let and const.

// During TDZ:
// - Variables are hoisted
// - But NOT initialized
// - Accessing them results in a ReferenceError

// Example 1:
console.log(a); // ❌ ReferenceError
let a = 10;

// Example 2:
{
  console.log(x); // ❌ ReferenceError (TDZ)
  let x = 5;
}

// Example 3:
{
  let y = 20;
  console.log(y); // ✅ 20 (outside TDZ)
}

// Key Points:
// - TDZ starts when scope is created
// - TDZ ends when variable is initialized
// - Only affects let and const (not var)

// Ans:
// Temporal Dead Zone is the phase between the creation of a scope and the initialization of variables declared with let and const, during which accessing them results in a ReferenceError.
