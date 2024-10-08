#!/usr/bin/python3
"""
This defines a Rectangle class.
The Rectangle class has private attributes for width and height,
and includes property methods for getting and setting these attributes
with validation to ensure they are positive integers.
"""


class Rectangle:
    """
    This defines the Rectangle class with width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.
        :param width: Optional; width of the rectangle (default is 0).
        :param height: Optional; height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This retrieves the width of the rectangle.
        :return: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This sets the width of the rectangle.
        :param value: The new width to set.
        :raises TypeError: If width is not an integer.
        :raises ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        This retrieves the height of the rectangle.
        :return: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This sets the height of the rectangle.
        :param value: The new height to set.
        :raises TypeError: If height is not an integer.
        :raises ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
