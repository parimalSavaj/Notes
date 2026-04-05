// call, apply, bind → used to control what "this" refers to inside a function

const serverLogger = {
  prefix: "[SERVER]",
  log: function (level, message) {
    console.log(`${this.prefix} [${level}]: ${message}`);

    // Check what "this" is
    console.log("This => ", this);
  },
};

const dbLogger = {
  prefix: "[DATABASE]",
};

// Normal function call
// "this" = serverLogger
serverLogger.log("a", "b");

// 1. call → Run immediately with custom "this"

/*
 call():
 - Runs the function instantly
 - First argument = what "this" should be
 - Remaining arguments = normal function inputs
*/

serverLogger.log.call(dbLogger, "ERROR", "Connection timeout");

// 2. apply → Same as call, but use array for arguments

/*
 apply():
 - Runs the function instantly
 - First argument = what "this" should be
 - Second argument = array of parameters

 Use when:
 - when you already have an array of data, like from an API response, and you want to pass it into a function without manually writing out data[0], data[1], data[2]
*/

serverLogger.log.apply(dbLogger, ["INFO", "Query executed successfully"]);

// 3. bind → Create function to use later

/*
 bind():
 - Does NOT run the function immediately
 - Returns a new function
 - "this" is permanently set (locked)

 Use when:
 - You want to reuse the function later
*/

const logToDB = serverLogger.log.bind(dbLogger);

logToDB("WARN", "High memory usage");
logToDB("ERROR", "Connection dropped");

// ===================== SUMMARY =====================

/*
Method | Executes Immediately? | How arguments are passed        | What it returns
------ | --------------------- | ------------------------------- | -------------------------
call   | Yes                   | Comma-separated (arg1, arg2)    | Result of the function
apply  | Yes                   | Array ([arg1, arg2])            | Result of the function
bind   | No                    | Comma-separated (arg1, arg2)    | A new, bound function
*/
