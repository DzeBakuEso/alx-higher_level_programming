#!/usr/bin/python3
"""Importing BaseGeometry the 7-base_geometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represent a rectangle inheriting frm BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.integer_validator("width", width)  # Validate width
        self.__width = width  # Set private attribute for width
        self.integer_validator("height", height)  # Validate height
        self.__height = height   # Set private attribute for height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
