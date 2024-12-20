#!/usr/bin/node

/**
 * Executes the provided function `x` times
 * @param {number} x - The number of times to execute the function
 * @param {function} theFunction - The function to be executed
 */
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

/**
 * Make the function available outside
 */
module.exports.callMeMoby = callMeMoby;
