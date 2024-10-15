#!/usr/bin/python3
"""
This module defines a function that checks if an object is
exactly an instance of a specified class.

Functions:
    is_same_class(obj, a_class): Returns True if the object
    is exactly an instance of the specified class, otherwise False.
"""


def is_same_class(obj, a_class):

    """
    This function checks if the given object is an instance
    of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is exactly an instance of a_class,
        otherwise False.
    """
    return type(obj) is a_class
