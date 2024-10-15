#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This defines a Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes the Rectangle with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):

        """Returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):

        """Calculates the area of the rectangle"""
        return self.__width * self.__height
