#!/usr/bin/node

/**
 * Function that returns a function to convert a number from base 10 to another base.
 * @param {number} base - The base to which the number will be converted.
 * @returns {function} - A function that takes a number and converts it to the specified base.
 */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);  // Convert number to the given base
  };
};
