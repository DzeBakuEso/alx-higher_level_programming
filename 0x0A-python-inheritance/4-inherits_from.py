#!/usr/bin/python3

"""
This module defines the function inherits_from.
The function determines if an object is an instance
of a class that inherited (directly or indirectly)
from a specified class.
"""


def inherits_from(obj, a_class):

    """
    This line checks if the object is an instance
    of a class that inherited from the given class.
    Returns True if the object inherits from a_class,
    but is not an exact instance of a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
