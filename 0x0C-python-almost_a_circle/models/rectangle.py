#!/usr/bin/python3
"""This module defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """This class represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This initializes a new Rectangle."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """This gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the width."""
        self.__width = value

    @property
    def height(self):
        """This gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the height."""
        self.__height = value

    @property
    def x(self):
        """This gets the x position."""
        return self.__x

    @x.setter
    def x(self, value):
        """This sets the x position."""
        self.__x = value

    @property
    def y(self):
        """This gets the y position."""
        return self.__y

    @y.setter
    def y(self, value):
        """This sets the y position."""
        self.__y = value
