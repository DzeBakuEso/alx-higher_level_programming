#!/usr/bin/python
"""
This is customized: This function appends a string to a text file (UTF-8)
and returns the number of characters added.
"""


def append_write(filename, text=""):

    """
    This is customized: Appends a string to the specified file.
    Args:
    filename (str): Name of the file to append to.
    text (str): The text content to append to the file.
    Returns:
    int: The number of characters added.
    Examples:
    >>> append_write("test_append_file.txt", "Hello!\n")
    7
    >>> append_write("test_append_file.txt", "New content.\n")
    14
    >>> with open("test_append_file.txt", 'r', encoding='utf-8') as f:
    ...     f.read()
    'Hello!\\nNew content.\\n'
    """
    # Using 'with statement to open the file in append mode'
    with open("file_append.txt" 'a', encoding='utf-8') as file:
        # Append the provided text to file and returns number of chaacters add
        return file.write(text)
