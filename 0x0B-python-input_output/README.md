Python Input/Output Project
Description
This project focuses on file handling, JSON serialization, and deserialization in Python. You'll be creating functions to read, write, append to files, and convert Python objects to and from JSON strings/files.

Requirements
Python Scripts
Editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All files must end with a new line
The first line of all Python scripts must be: #!/usr/bin/python3
A README.md file at the root of the project folder is mandatory
Your code should follow pycodestyle (version 2.8.*)
All files must be executable
File length will be checked using the wc command
Python Test Cases
Editors: vi, vim, emacs
All files should end with a new line
All test files should be inside a tests folder
Test files should be text files with the .txt extension
Tests should be executed using: python3 -m doctest ./tests/*
All modules should have proper documentation
All classes should have proper documentation
All functions (inside and outside classes) must have proper documentation
Documentation must be comprehensive, explaining the purpose of each module, class, and method
Tasks
0. Read file
Write a function that reads a text file (UTF8) and prints it to stdout.
Prototype: def read_file(filename=""):
1. Write to a file
Write a function that writes a string to a text file (UTF8) and returns the number of characters written.
Prototype: def write_file(filename="", text=""):
2. Append to a file
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
Prototype: def append_write(filename="", text=""):
3. To JSON string
Write a function that returns the JSON representation of an object (string).
Prototype: def to_json_string(my_obj):
4. From JSON string to Object
Write a function that returns a Python data structure represented by a JSON string.
Prototype: def from_json_string(my_str):
5. Save Object to a file
Write a function that writes a Python object to a text file using JSON representation.
Prototype: def save_to_json_file(my_obj, filename):
6. Create object from a JSON file
Write a function that creates an object from a “JSON file”.
Prototype: def load_from_json_file(filename)
