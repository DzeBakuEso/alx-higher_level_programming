#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Function that prints an integer with error handling."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
