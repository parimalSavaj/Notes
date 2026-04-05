// The splice() method in JavaScript is used to add, remove, or replace elements within an array. Unlike slice(), which creates a shallow copy and does not alter the original array, splice() modifies the original array in place and returns an array containing the removed elements.

/* Syntax
array.splice(start, deleteCount, item1, item2, ...)
*/

// - start: The index at which to start changing the array.
// - deleteCount: (Optional) The number of elements to remove from the array. If omitted, all elements from the start index to the end of the array will be removed.
// - item1, item2, ...: (Optional) Elements to add to the array, starting at the start position.

let arrayIntegersOriginal1 = [1, 2, 3, 4, 5];
let arrayIntegersOriginal2 = [1, 2, 3, 4, 5];
let arrayIntegersOriginal3 = [1, 2, 3, 4, 5];

// Remove the first two elements
let arrayIntegers1 = arrayIntegersOriginal1.splice(0, 2);
// arrayIntegers1: [1, 2]
// arrayIntegersOriginal1 (after): [3, 4, 5]

// Remove all elements from index 3 onwards
let arrayIntegers2 = arrayIntegersOriginal2.splice(3);
// arrayIntegers2: [4, 5]
// arrayIntegersOriginal2 (after): [1, 2, 3]

// Remove 1 element at index 3, then insert "a", "b", "c" at that position
let arrayIntegers3 = arrayIntegersOriginal3.splice(3, 1, "a", "b", "c");
// arrayIntegers3: [4]
// arrayIntegersOriginal3 (after): [1, 2, 3, "a", "b", "c", 5]

/* 
Note:
The splice() method modifies the original array.
It returns an array containing the elements that were removed (if any).
You can use it both to remove and insert elements in a single operation.
*/
