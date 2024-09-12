#!/usr/bin/python3


import importlib.util
import sys


def main():
    # Path to the hidden_4.pyc file
    path = './hidden_4.pyc'

    # Load the .pyc file
    spec = importlib.util.spec_from_file_location("hidden_4", path)
    hidden_4 = importlib.util.module_from_spec(spec)
    sys.modules["hidden_4"] = hidden_4
    spec.loader.exec_module(hidden_4)

    # Get all attributes of the hidden_4 module
    names = dir(hidden_4)

    # Filter out names that start with '__'
    public_names = [name for name in names if not name.startswith('__')]

    # Print names sorted in alphabetical order
    for name in sorted(public_names):
        print(name)


if __name__ == "__main__":
    main()
