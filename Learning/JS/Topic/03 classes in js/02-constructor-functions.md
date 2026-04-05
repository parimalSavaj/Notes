# Constructor Functions (The Blueprint)

A Constructor Function is a special type of function used as a "blueprint" to create multiple objects that have the exact same structure.

## 1. How to write a Constructor Function

- **Rule 1:** The function name should always start with a Capital letter (this tells other developers it is a blueprint, not a normal function).
- **Rule 2:** You use the `this` keyword inside the function to assign values to the object being created.

```javascript
function User(userName, userAge) {
  this.name = userName;
  this.age = userAge;

  this.sayHello = function () {
    console.log("Hi, I am " + this.name);
  };
}
```

## 2. The new Keyword (The Magic Word)

To actually build an object from your blueprint, you MUST use the new keyword when calling the function.

```JavaScript
const user1 = new User("Alex", 25);
const user2 = new User("Sam", 30);

user1.sayHello(); // "Hi, I am Alex"
user2.sayHello(); // "Hi, I am Sam" 3. What does new actually do?
```

When you write new User(), JavaScript automatically does three important things behind the scenes:

- It creates a brand new, empty object {}.

- It takes the this keyword inside the function and points it to that new empty object.

- It automatically returns the object at the end of the function (so you don't have to write return this;).

---
