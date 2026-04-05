# Understanding JavaScript Objects

In JavaScript, an object is a standalone entity that holds multiple values. It is like a container that stores related data and functionality together.

Instead of storing a single value like a string or number, an object stores data in **key-value pairs**.

## 1. Creating an Object (Object Literal)

The simplest way to create an object is using curly braces `{}` it's call `Object Literal`.

```javascript
const user = {
  name: "Alex",
  age: 25,
  role: "Backend Developer",
};
```

## 2. Accessing Properties

You can read the data inside an object in two ways:

Dot Notation (Most Common): console.log(user.name); // "Alex"

Bracket Notation: console.log(user["age"]); // 25 (Useful when the key is stored in a variable).

## 3. Modifying an Object

Objects are dynamic. You can easily add, update, or delete properties after the object is created.

```JavaScript
// Update an existing property
user.age = 26;

// Add a brand new property
user.country = "India";

// Delete a property
delete user.role;
```

## 4. Methods (Functions inside Objects)

Objects can also hold functions. When a function is inside an object, it is called a method.

```JavaScript
const user = {
name: "Alex",
sayHello: function() {
// 'this' refers to the object itself
console.log("Hello, my name is " + this.name);
}
};

user.sayHello(); // Output: Hello, my name is Alex
```

**`The Problem: If you want to create 100 users, writing out this entire object literal 100 times is terrible for your code. That is why we use Constructor Functions.`**

---
