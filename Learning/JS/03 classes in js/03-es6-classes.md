# ES6 Classes (The Modern Syntax)

JavaScript Classes were introduced in ES6 (2015). **Classes do not change how JavaScript works under the hood.** They are just "syntactic sugar" — a cleaner, more readable way to write Constructor Functions.

## 1. How to write a Class

Instead of using the `function` keyword, you use the `class` keyword.

Inside the class, you use a special method called `constructor()`. This is where you pass your data, exactly like you did in the old Constructor Function.

```javascript
class User {
  // 1. The constructor method replaces the old function body
  constructor(userName, userAge) {
    this.name = userName;
    this.age = userAge;
  }

  // 2. Methods are written directly inside the class
  sayHello() {
    console.log("Hi, I am " + this.name);
  }
}
```

## 2. Creating an Object from a Class

You create an instance (an object) from a class exactly the same way you did with a Constructor Function: by using the new keyword.

```JavaScript
const user1 = new User("Alex", 25);
const user2 = new User("Sam", 30);

user1.sayHello(); // "Hi, I am Alex"
```

## 3. Why use Classes?

It is much easier to read and organize code.

It looks exactly like Object-Oriented Programming in other languages (like Java, Python, or C++), making it easier for developers to learn.

All of your setup (the constructor) and all of your actions (the methods) are wrapped up neatly inside one clean block of code.
