#!/usr/bin/node
const BaseSquare = require('./5-square');

/**
 * Defines a Square class that inherits from the Square class (from 5-square.js).
 */
class Square extends BaseSquare {
  /**
   * Method to print the square with a given character.
   * @param {string} c - The character used to print the square.
   */
  charPrint (c) {
    const character = c || 'X'; // Default to 'X' if no character is provided
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width)); // Print one row of the square
    }
  }
}

module.exports = Square;
