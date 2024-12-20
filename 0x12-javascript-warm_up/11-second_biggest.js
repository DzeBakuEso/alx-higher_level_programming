#!/usr/bin/node

/**
 * Function to find the second biggest integer in the argument list.
 *
 * @param {Array} args - The array of arguments passed to the script.
 * @returns {number} - The second biggest integer, or 0 if not applicable.
 */
function secondBiggest (args) {
  /* Convert all argunts to integers & remove first two items (script name) */
  const numbers = args.slice(2).map(arg => parseInt(arg));

  /* If there are less than two numbers, return 0 */
  if (numbers.length < 2) {
    return 0;
  }

  /* Sort the array in descending order */
  numbers.sort((a, b) => b - a);

  /* Return the second largest number */
  return numbers[1];
}

/**
 * Get the arguments passed to the script and compute the second biggest number.
 */
const result = secondBiggest(process.argv);

/* Print the result */
console.log(result);
