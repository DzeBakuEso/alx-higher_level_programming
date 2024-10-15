"""This defines a fnx @ saves object to text file using JSON reprttion."""


import json  # This is needed for JSON serialization


def save_to_json_file(my_obj, filename):
    """This writes an Object to a text file, using JSON repreation."""
    with open("my_list.json", 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)  # Serialize and write the object to the file
