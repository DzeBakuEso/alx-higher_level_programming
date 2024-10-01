#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute 'size'.
"""


class Square:
    """
    A class used to represent a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
