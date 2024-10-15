#!/usr/bin/python3
"""Importing Rectangle frm the 9-rectangle module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represnts square inheriting frm Rectangle."""

    def __init__(self, size):
        """Initialize the square with size."""
        self.integer_validator("size", size)  # Validate size
        self.__size = size  # Set private attribute for size
        super().__init__(size, size)  # ith width height = to size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
