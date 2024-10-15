#!/usr/bin/python3
"""This module defines a function to convert an object to a JSON string."""


import json


def to_json_string(my_obj):
    """This defines a function that converts an object to a JSON string."""
    return json.dumps(my_obj)
