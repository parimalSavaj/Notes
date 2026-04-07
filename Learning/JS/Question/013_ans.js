// ES Modules → split code into reusable files

// Uses:
// - export → send data
// - import → use data

// ========================================
// 1. Exporting (utils.js)
// ========================================

// Named exports
export const add = (a, b) => a + b;
export const multiply = (a, b) => a * b;

// Default export (only one allowed per file)
export default function greet(name) {
  return `Hello, ${name}`;
}

// ========================================
// 2. Importing (app.js)
// ========================================

import greet, { add, multiply } from "./utils.js";

console.log(add(2, 3));
console.log(multiply(2, 3));
console.log(greet("Jasmin"));

// ========================================
// Named vs Default
// ========================================

/*
Named Export:
- Multiple allowed
- Use {} to import
- Name must match (or rename using { add as sum })

Example:
import { add } from "./utils.js";
import { add as sum } from "./utils.js";

Default Export:
- Only one per file
- No {}
- Can use any name

Example:
import greet from "./utils.js";
import sayHello from "./utils.js";
*/

// ========================================
// Dynamic Import (lazy loading)
// ========================================

const module = await import("./utils.js");

console.log(module.add(2, 3));

// ========================================
// ES Modules vs CommonJS
// ========================================

/*
ES Modules:
- import / export
- Async
- Used in modern JS

CommonJS:
- require() / module.exports
- Sync
- Old Node.js
*/

// ========================================
// Enable ES Modules
// ========================================

// Node.js
// package.json → { "type": "module" }

// Browser
// <script type="module" src="app.js"></script>

// ========================================
// INTERVIEW POINTS
// ========================================

/*
- Named → multiple, {} required
- Default → single, no {}
- import() → async (lazy load)
- require() → sync
*/
