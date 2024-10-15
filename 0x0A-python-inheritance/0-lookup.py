#!/usr/bin/python3
# This line defines the lookup function, which takes an object as an argument.
def lookup(obj):
    # This line returns the list of available attributes and methods
    # of the provided object using the dir() function.
    return dir(obj)
