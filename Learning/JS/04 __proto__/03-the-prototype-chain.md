# The Prototype Chain

The Prototype Chain is the mechanism JavaScript uses to find methods and properties. It acts like a detective following a trail of clues.

## How the Lookup Process Works
When you try to call a method on an object (like `user1.sayHello()`), the JavaScript engine follows these exact steps:

1. **Check the Object Itself:** "Does `user1` have a function called `sayHello` directly inside it?" 
   *(No, it only has the `name` property).*

2. **Follow the `__proto__` string:** Because it didn't find the method, the engine follows the invisible string up to the creator's backpack (`User.prototype`).

3. **Check the Backpack:** "Is `sayHello` inside this backpack?" 
   *(Yes!)* The engine finds the method and runs it.

## What if it isn't in the first backpack?
If the engine doesn't find the method in `User.prototype`, it doesn't give up. 
Because `User.prototype` is *also* an object, it has its own `__proto__` string connecting it to the master `Object.prototype` at the very top of JavaScript.

The engine will keep following the chain upwards:
`user1`  -->  `User.prototype`  -->  `Object.prototype`  -->  `null`

If it reaches the very end of the chain (`null`) and still hasn't found the method, it will return `undefined` or throw a "not a function" error. This upward journey is called the **Prototype Chain**.