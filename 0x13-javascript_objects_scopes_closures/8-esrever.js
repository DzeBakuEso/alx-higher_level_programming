#!/usr/bin/node

/**
 * Function that returns the reversed version of a list without using the built-in reverse method.
 * @param {Array} list - The list to be reversed.
 * @returns {Array} A new array with the elements of the original list in reversed order.
 */
exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
