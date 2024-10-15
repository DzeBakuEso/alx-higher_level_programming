#!/usr/bin/python3
"""
This defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """
    A class BaseGeometry with a method that raises an exception
    when called, as it is not implemented.
    """

    def area(self):

        """
        Public instance method that raises an Exception to indicate
        that the area method is not yet implemented.
        """
        raise Exception("area() is not implemented")
