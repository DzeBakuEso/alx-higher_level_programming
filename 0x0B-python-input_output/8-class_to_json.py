#!/usr/bin/python3
"""This module defines a function to convert class attributes to a JSON serializable dictionary."""


def class_to_json(obj):

    """Return the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing serializable attributes of the object.
    """
    # Initialize an empty dictionary to hold serializable attributes
    return {k: v for k, v in obj.__dict__.items() if isinstance(v, (list, dict, str, int, bool))}
