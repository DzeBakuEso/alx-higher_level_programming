#!/usr/bin/node

let count = 0; // Variable to keep track of the number of arguments printed

/**
 * Function that logs the count of arguments already printed and the current argument value.
 * @param {any} item - The argument to be printed.
 */
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++; // Increment the count after printing the argument
};
