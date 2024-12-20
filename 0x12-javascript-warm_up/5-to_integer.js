#!/usr/bin/node

/**
 * Tries to convert the first argument to an integer and prints it.
 * If the argument cannot be converted to an integer, prints "Not a number".
 */

const arg = process.argv[2];
const num = parseInt(arg);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:' + num);
}
