#!/usr/bin/python3
"""
This defines a Rectangle class with methods for area, perimeter,
and string representation.
"""


class Rectangle:
    """This defines a rectangle by its width and height."""

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with width and height.
        
        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """This returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """This returns the string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """This returns a string representation of the rectangle for debugging."""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"
