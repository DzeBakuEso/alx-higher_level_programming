#!/usr/bin/python3
def no_c(my_string):
    # Initialize an empty string to build the result
    result = ""

    # Iterate through each character in the input string
    for char in my_string:
        # Append characters that are not 'c' or 'C' to the result string
        if char not in ('c', 'C'):
            result += char

    return result
