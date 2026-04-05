/*

In JavaScript, most things are objects.

Every object has a hidden link to another object. This is called its *prototype*.

When you try to use a property or method, JavaScript looks for it like this:

* First, it checks the object itself. If found, it uses it.
* If not found, it looks in the object’s prototype.
* If still not found, it looks in the prototype’s prototype.
* This keeps going until it reaches the end (where prototype is null).
* If it still doesn’t find it, JavaScript returns undefined.

*/

class Employee {
  constructor(name) {
    this.name = name;
  }

  clockIn() {
    return `${this.name} has clocked in.`;
  }
}

class BackendDeveloper extends Employee {
  constructor(name, language) {
    super(name);
    this.language = language;
  }

  writeCode() {
    return `${this.name} is writing APIs in ${this.language}.`;
  }
}

console.log(BackendDeveloper.prototype);
const myObject = new ChildClass();

console.log(myObject.__proto__ === ChildClass.prototype); // True
console.log(myObject.__proto__.__proto__ === ParentClass.prototype); // True

// Class → has prototype
// Object or any Variable → has __proto__
