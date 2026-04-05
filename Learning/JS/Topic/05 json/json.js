// JSON (JavaScript Object Notation)

/*
 JSON is a simple format to store and send data
 It looks like JavaScript objects (key-value pairs)

 Used for:
 - Sending data between server and client
 - Storing data

 File extension → .json
 Type → application/json
*/

// ===================== PARSING =====================

/*
 Parsing = Convert JSON string → JavaScript object

 Use when:
 - You receive data (API, server)
*/

const jsonString = '{"name":"John","age":30}';

// Convert string to object
const obj = JSON.parse(jsonString);

// Result → { name: "John", age: 30 }

// ===================== STRINGIFY =====================

/*
 Stringify = Convert JavaScript object → JSON string

 Use when:
 - Sending data to server
 - Saving data
*/

const user = { name: "Jane", age: 25 };

// Convert object to string
const jsonData = JSON.stringify(user);

// Result → '{"name":"Jane","age":25}'

// ===================== QUICK SUMMARY =====================

/*
Operation    | What it does                         | Method
------------ | ------------------------------------ | -------------------
Parsing      | JSON string → JavaScript object      | JSON.parse()
Stringify    | JavaScript object → JSON string      | JSON.stringify()
*/
