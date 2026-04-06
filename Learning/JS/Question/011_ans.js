// Shallow Copy vs Deep Copy (Important Interview Topic)

// Core Idea:
// - Objects store reference (memory address)
// - Problem happens with nested objects

// ========================================
// Shallow Copy → shares nested reference
// ========================================

const originalUser = {
  name: "Alex",
  address: {
    city: "London",
  },
};

const shallowCopy = { ...originalUser };

// Change top-level
shallowCopy.name = "John";

// Change nested
shallowCopy.address.city = "Sydney";

console.log(originalUser.name); // "Alex" ✅ safe
console.log(originalUser.address.city); // "Sydney" ❗ changed

// Reason:
// - Nested object is shared (same memory)

// ========================================
// Deep Copy → fully independent copy
// ========================================

const deepCopy = structuredClone(originalUser);

// Change nested
deepCopy.address.city = "Delhi";

console.log(originalUser.address.city); // "Sydney" (unchanged)
console.log(deepCopy.address.city); // "Delhi"

// Reason:
// - Everything is copied (no shared reference)

// ========================================
// Methods
// ========================================

/*
Shallow:
- { ...obj }
- Object.assign()
- slice(), Array.from()

Deep:
- structuredClone() ✅ (modern)
- JSON.parse(JSON.stringify()) ❌ (old, limited)
*/

// ========================================
// JSON method limitations
// ========================================

/*
- Removes undefined, functions
- Date → string
- No Map, Set
- Fails for circular objects
*/

// ========================================
// INTERVIEW POINTS
// ========================================

/*
Shallow:
- Copies top-level only
- Nested → shared reference

Deep:
- Copies everything
- Fully independent

Performance:
- Shallow → fast
- Deep → slower

Rule:
- Nested object → use deep copy
*/
