#!/usr/bin/python3
"""
This is customized: This function writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):

    """
    This is customized: Writes a string to the specified file.
    Args:
    filename (str): Name of the file to write to.
    text (str): The text content to write into the file.
    Returns:
    int: The number of characters written.
    """
    # Using 'with' statement to open the file in write mode
    with open("my_first_file.txt", 'w', encoding='utf-8') as file:
        # Write the provided text to the file and return number of characters
        return file.write(text)