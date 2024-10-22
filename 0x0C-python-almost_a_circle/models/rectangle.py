#!/usr/bin/python3
"""This module defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """This class represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This initializes a new Rectangle."""
        self.width = width  # Will call the setter and validate
        self.height = height  # Will call the setter and validate
        self.x = x  # Will call the setter and validate
        self.y = y  # Will call the setter and validate
        super().__init__(id)

    @property
    def width(self):
        """This gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This gets the x position."""
        return self.__x

    @x.setter
    def x(self, value):
        """This sets the x position."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This gets the y position."""
        return self.__y

    @y.setter
    def y(self, value):
        """This sets the y position."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This calculates the area of the rectangle."""
        return self.width * self.height
