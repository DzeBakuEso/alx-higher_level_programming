#!/usr/bin/python3  # Shebang to specify Python interpreter

# Print numbers from 0 to 98 in decimal and hexadecimal
for number in range(99):
    print("{:d} = 0x{:x}".format(number, number))

