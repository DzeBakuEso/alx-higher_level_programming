#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/**
 * Defines a Square class that inherits from Rectangle.
 */
class Square extends Rectangle {
  /**
   * Constructor that initializes the square's size.
   * @param {number} size - The size of the square.
   */
  constructor (size) {
    super(size, size); // Call the constructor of Rectangle with equal width and height
  }
}

module.exports = Square;
