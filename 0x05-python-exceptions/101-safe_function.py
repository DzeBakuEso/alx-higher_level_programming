#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely and returns the result or None on failure."""
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
