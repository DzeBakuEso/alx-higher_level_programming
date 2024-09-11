#!/usr/bin/python3  # Shebang to specify Python interpreter

# Print all unique combinations of two different digits
for i in range(10):
    for j in range(i + 1, 10):
        # Print the combination formatted as two digits
        if i != 9 or j != 9:  # To avoid trailing comma and space on the last combination
            print("{:02d}, ".format(i * 10 + j), end='')
        else:
            print("{:02d}".format(i * 10 + j))

