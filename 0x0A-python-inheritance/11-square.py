#!/usr/bin/python3
"""Importing Rectangle from the 9-rectangle module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that repress a square inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize the square with size."""
        self.integer_validator("size", size)  # Validate size
        self.__size = size   # Set private attribute for size
        super().__init__(size, size)  # Inze the Regle wight equal to size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
