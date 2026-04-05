# "Everything in JavaScript is an Object"

You will often hear that "everything in JavaScript is an object." While there are primitive data types (like strings, numbers, and booleans), JavaScript treats almost everything you interact with as an object under the hood.

## 1. Arrays are Objects

When you create an array, you are actually creating a specific type of object. This is why you can use built-in methods on them.

```javascript
const myArray = [1, 2, 3];
myArray.push(4); // .push() is a method hidden inside the Array object
```

## 2. Functions are Objects

In JavaScript, functions are "first-class citizens" and behave like objects. You can actually attach properties directly to a function!

```JavaScript
function sayHi() { console.log("Hi"); }
sayHi.language = "English"; // Adding a property to a function!
```

## 3. Primitives act like Objects

When you call a method on a simple string or number, JavaScript temporarily wraps that primitive value in an invisible "Object Wrapper" just long enough to use the method, and then throws the wrapper away.

```JavaScript
const myName = "alex";
console.log(myName.toUpperCase()); // "ALEX"
// JavaScript temporarily turned "alex" into a String Object to find the .toUpperCase() method.
```

Ultimately, Arrays, Functions, and wrapped Primitives all link back to one master parent at the very top of JavaScript: the master Object.

---
