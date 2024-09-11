#!/usr/bin/python3  # Shebang to specify Python interpreter

# Print numbers from 0 to 99 separated by ", " and end with a newline
for number in range(100):
    # Print the number with leading zeros, followed by a comma and space
    # Use `end=''` to avoid adding extra newlines
    if number != 99:
        print("{:02d}, ".format(number), end='')
    else:
        print("{:02d}".format(number))

