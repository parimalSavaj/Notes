// Template Literals & Tagged Templates

// ========================================
// Template Literals → backticks ` `
// ========================================

// Insert variables using ${}

const name = "Justin";
console.log(`Hello, ${name}`); // Hello, Justin

// Expressions also work
const a = 5;
const b = 3;

console.log(`Sum is ${a + b}`); // 8
console.log(`Result is ${a > b ? "Yes" : "No"}`); // Yes

// Multi-line string (no \n needed)
const text = `Line 1
Line 2`;

// ========================================
// Tagged Templates → function + template
// ========================================

function tag(strings, ...values) {
  console.log(strings); // static parts
  console.log(values); // dynamic values
}

tag`Hello ${"Justin"}, you have ${3} messages`;

// Output:
// strings → ["Hello ", ", you have ", " messages"]
// values → ["Justin", 3]

// ========================================
// Use Case: sanitize input (security)
// ========================================

function safeHTML(strings, ...values) {
  const escape = (str) => str.replace(/</g, "&lt;").replace(/>/g, "&gt;");

  return strings.reduce((res, str, i) => {
    const val = values[i] ? escape(String(values[i])) : "";
    return res + str + val;
  }, "");
}

const userInput = "<script>alert(1)</script>";

const output = safeHTML`<p>${userInput}</p>`;

console.log(output);
// "<p>&lt;script&gt;alert(1)&lt;/script&gt;</p>"

// ========================================
// INTERVIEW POINTS
// ========================================

/*
Template Literals:
- Use backticks ``
- ${} for variables/expressions
- Supports multi-line

Tagged Templates:
- Function processes template
- Gets (strings, values) separately
- Useful for sanitization, formatting
*/
