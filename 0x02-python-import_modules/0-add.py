#!/usr/bin/python3
# Import the add function from add_0 module


from add_0 import add


# Assign values to variables a and b
a = 1
b = 2

# Print the result of the addition in the required format
print("{} + {} = {}".format(a, b, add(a, b)))

# Ensure that this script doesn't execute when imported
if __name__ == "__main__":
    pass
