#!/usr/bin/python3


import sys


def main():
    # Get the list of arguments excluding the script name
    args = sys.argv[1:]

    # Convert all arguments to integers and sum them up
    total = sum(int(arg) for arg in args)

    # Print the result
    print(total)


if __name__ == "__main__":
    main()
