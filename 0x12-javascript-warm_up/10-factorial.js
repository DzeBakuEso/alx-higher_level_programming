#!/usr/bin/node

/**
 * Computes the factorial of a given number recursively.
 *
 * @param {number} n - The number to compute the factorial of.
 * @returns {number} - The factorial of the number.
 */
function factorial (n) {
  if (isNaN(n) || n <= 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

/**
 * Get the argument passed to the script and convert it to an integer.
 */
const num = parseInt(process.argv[2]);

/* Call the factorial function and print the result */
console.log(factorial(num));
