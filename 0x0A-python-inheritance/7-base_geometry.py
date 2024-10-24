#!/usr/bin/python3
"""
This defines a class BaseGeometry with methods to calculate area
and validate integers.
"""


class BaseGeometry:
    """
    A class BaseGeometry with methods for area calculation
    and integer validation.
    """

    def area(self):

        """
        Public instance method that raises an Exception to indicate
        that the area method is not yet implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer and greater than 0.
        Args:
            name (str): The name of the value (used in exception messages).
            value (int): The value to validate.
        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
