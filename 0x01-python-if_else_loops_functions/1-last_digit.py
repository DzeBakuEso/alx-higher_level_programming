#!/usr/bin/python3  # Shebang to specify Python interpreter

import random  # Import the random module to generate random numbers

# Generate a random integer between -10000 and 10000
number = random.randint(-10000, 10000)

# Get the last digit, taking care of negative numbers
if number < 0:
    last_digit = abs(number) % 10  # Get the last digit for negative numbers
    last_digit = -last_digit  # Make it negative if the number is negative
else:
    last_digit = number % 10  # Get the last digit for positive numbers

# Prepare the output
print(f"Last digit of {number} is {last_digit}", end=" ")

# Check conditions and print the corresponding output
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

