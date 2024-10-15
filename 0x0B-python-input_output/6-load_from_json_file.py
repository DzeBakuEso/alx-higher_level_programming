"""This defines a fnx that loads object from JSON file."""


import json  # This is needed for JSON deserialization


def load_from_json_file(filename):
    """This creates an Object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)  # Read and deserialize the JSON content
