// The slice() method in JavaScript is used to extract a section of an array, returning a new array containing the selected elements. It does not modify the original array. The method takes two arguments:

// - start: The index at which extraction begins (inclusive).
// - end (optional): The index before which to end extraction (exclusive). If omitted, extraction continues to the end of the array.
// You can also use negative indices, which count from the end of the array.

let arrayIntegers = [1, 2, 3, 4, 5];

let arrayIntegers1 = arrayIntegers.slice(0, 2); // [1, 2]
let arrayIntegers2 = arrayIntegers.slice(2, 3); // [3]
let arrayIntegers3 = arrayIntegers.slice(4); // [5]
let arrayIntegers4 = arrayIntegers.slice(-3, -1); // [3, 4]

/* 
Note:
The slice() method does not mutate (change) the original array; instead, it returns a new array containing the extracted elements.
 */
