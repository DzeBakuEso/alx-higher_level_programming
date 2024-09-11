#!/usr/bin/python3  # Shebang to specify Python interpreter

def print_last_digit(number):
    """Prints the last digit of a number and returns it."""
    # Get the last digit. Use abs() to handle negative numbers.
    last_digit = abs(number) % 10
    print(last_digit, end='')
    return last_digit

