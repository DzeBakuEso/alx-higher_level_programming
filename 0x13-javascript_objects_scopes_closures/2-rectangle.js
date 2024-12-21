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
}

module.exports = Rectangle;
