"""This defines a function @ converts a JSON string to a Python object."""


import json  # This is needed for JSON deserialization


def from_json_string(my_str):
    """This returns object (Python data strture) represntd by JSON strng."""
    return json.loads(my_str)  # Convert JSON string to Python object
