#!/usr/bin/python3

"""
This module provides a fnx to return list of attributes,methods of an object.

Functions:
    lookup(obj): Returns a list of attributes and methods of the given object.
"""


def lookup(obj):

    """
    This function returns the list of attributes and methods of an object.

    Args:
        obj (object): The object whose attributes,methods are to be retrieved.

    Returns:
        list: A list of strings representing the attributes and methods.
    """
    return dir(obj)
