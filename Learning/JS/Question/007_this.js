// "this" → refers to the object that calls the function

// Rule:
// Check object BEFORE the dot (.)

// ========================================
// Example 1: Global context
// ========================================

function test() {
  console.log(this);
}

test();
// In browser → window (global object)

// ========================================
// Example 2: Object method
// ========================================

const obj = {
  name: "Vivek",
  getName: function () {
    console.log(this.name);
  },
};

obj.getName(); // Vivek

// "this" = obj

// ========================================
// Example 3: Function reassigned
// ========================================

const obj1 = {
  name: "Vivek",
  getName: function () {
    console.log(this.name);
  },
};

const obj2 = {
  name: "Akshay",
};

obj2.getName = obj1.getName;

obj2.getName(); // Akshay

// "this" = obj2 (caller object)

// ========================================
// Example 4: Missing property
// ========================================

const user1 = {
  address: "Mumbai",
  getAddress: function () {
    console.log(this.address);
  },
};

const user2 = {
  name: "Akshay",
};

user2.getAddress = user1.getAddress;

user2.getAddress(); // undefined

// "this" = user2
// but user2.address doesn't exist

// ========================================
// Key Rules
// ========================================

/*
1. this = object before dot
2. No object → global object (window)
3. Value depends on how function is called
4. Can change using call, apply, bind
*/

// ========================================
// INTERVIEW TIP
// ========================================

// "this" is decided at runtime (call time)
