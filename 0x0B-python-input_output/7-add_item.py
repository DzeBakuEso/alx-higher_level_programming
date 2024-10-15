#!/usr/bin/python3
"""This script adds all argum to Python list & saves them to file."""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
import os


# Define the filename to save the list
filename = "add_item.json"

# Check if the file exists
if os.path.exists(add_item.json):
    # Load existing data from the JSON file
    items = load_from_json_file(add_item.json)
else:
    # Create a new list if the file does not exist
    items = []

# Add all arguments (excluding the script name) to the list
items.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(items, add_item.json)
