#!/usr/bin/python3
# Importing the add function from add_0.py
from add_0 import add

# Define variables
a = 1
b = 2

# Call the add function and print the result
print(f"{a} + {b} = {add(a, b)}")

# Ensure the script is not executed when imported
if __name__ == "__main__":
    pass

