#!/usr/bin/node

/**
 * Function that counts the number of occurrences of a search element in a list.
 * @param {Array} list - The list in which to count occurrences.
 * @param {*} searchElement - The element whose occurrences will be counted.
 * @returns {number} The number of occurrences of searchElement in the list.
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
