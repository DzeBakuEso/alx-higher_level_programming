#!/usr/bin/python
from models.base import Base  # Ensure this line is present


class Rectangle(Base):
    """This represents a rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This initializes the rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This returns the width."""
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
        """This returns the height."""
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
        """This returns the x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """This sets the x coordinate."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This returns the y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """This sets the y coordinate."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """This prints the rectangle using the character #."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """This returns a string representation of the rectangle."""
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args):
        """This updates the attributes of the rectangle."""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
