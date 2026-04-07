// Optional Chaining (?.) & Nullish Coalescing (??)

// ========================================
// Optional Chaining (?.) → safe access
// ========================================

// Avoid error when nested property may not exist

const user = {
  profile: {
    address: {
      city: "Mumbai",
    },
  },
};

console.log(user.profile.address?.city); // "Mumbai"

// If address missing
const user2 = {
  profile: {},
};

console.log(user2.profile.address?.city); // undefined (no error)

// ========================================
// Where to use ?.
// ========================================

obj?.a?.b; // property
obj?.method(); // method
arr?.[0]; // array

// Stops if null/undefined

// ❌ Not allowed in assignment
// user?.name = "John";

// ========================================
// Nullish Coalescing (??) → fallback value
// ========================================

const name = null;
console.log(name ?? "Guest"); // "Guest"

// ========================================
// ?? vs ||
// ========================================

const config = { port: 0 };

// || → checks falsy values
const port1 = config.port || 3000;
console.log(port1); // 3000 ❗ (0 ignored)

// ?? → checks only null/undefined
const port2 = config.port ?? 3000;
console.log(port2); // 0 ✅

// ========================================
// Combine both
// ========================================

const city = user2.profile?.address?.city ?? "Not Available";

console.log(city); // "Not Available"

// ========================================
// INTERVIEW POINTS
// ========================================

/*
?. :
- Safe access
- Prevents errors
- Returns undefined if missing

?? :
- Provides default value
- Only for null/undefined

Difference:
|| → checks falsy (0, "", false)
?? → checks only null/undefined
*/
