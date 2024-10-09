#!/usr/bin/python3
class Rectangle:
    """ This defines a Rectangle class """

    # Public class attribute, initialized to 0
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializes a rectangle with width and height """
        self.width = width
        self.height = height
        # Increment the class attribute when a new instance is created
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ This defines the width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ This sets the width property """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ This defines the height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ This sets the height property """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ This calculates the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ This calculates the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ String representation of the rectangle using '#' """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """ Returns the formal string represe to recreate a new instance """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Destructor that prints a messa and decrem number_of_instances """
        print("Bye rectangle...")
        # Decrement the class attribute when an instance is deleted
        Rectangle.number_of_instances -= 1
