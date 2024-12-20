#!/usr/bin/node

/**
 * Adds two integers a and b and prints the result.
 *
 * @param {number} a - The first integer.
 * @param {number} b - The second integer.
 * @returns {number} - The sum of a and b.
 */
function add (a, b) {
  return a + b;
}

/**
 * Get the arguments passed to the script and convert them to integers.
 */
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

/* Ensure that both arguments are valid numbers */
if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
