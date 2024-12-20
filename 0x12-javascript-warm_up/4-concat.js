#!/usr/bin/node

/**
 * Prints two arguments passed to the script in the format "arg1 is arg2".
 * If an argument is missing, it will print "undefined" for that argument.
 */

console.log(process.argv[2] + ' is ' + process.argv[3]);
