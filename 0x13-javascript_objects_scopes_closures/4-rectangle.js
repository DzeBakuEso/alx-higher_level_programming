#!/usr/bin/node
/**
 * Defines a class Rectangle.
 */
class Rectangle {
  /**
   * Constructor that initializes the rectangle's width and height.
   * If w or h is 0 or not a positive integer, an empty object is created.
   * @param {number} w - The width of the rectangle.
   * @param {number} h - The height of the rectangle.
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
   * Prints the rectangle using the character 'X'.
   */
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  /**
   * Rotates the rectangle by swapping its width and height.
   */
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  /**
   * Doubles the size of the rectangle.
   * Multiplies both width and height by 2.
   */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
