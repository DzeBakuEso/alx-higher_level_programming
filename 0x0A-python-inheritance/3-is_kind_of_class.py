#!/urs/bin/python3
"""
This module defines a function to check if an object is
an instance of, or inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):

    """
    This function checks if the object `obj` is an instance
    of the class `a_class`, or if it is an instance of a class
    that inherited from `a_class`.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if `obj` is an instance of `a_class` or
        a subclass of `a_class`, otherwise False.
    """
    return isinstance(obj, a_class)
