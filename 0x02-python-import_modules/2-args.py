#!/usr/bin/python3


import sys


def main():
    # Get the list of arguments
    args = sys.argv[1:]

    # Get the number of arguments
    num_args = len(args)

    # Print the number of arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    # Print each argument with its position
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
