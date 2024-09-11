#!/usr/bin/python3  # Corrected shebang

import random  # Import the random module to generate random numbers

number = random.randint(-10, 10)  # Generate a random integer between -10 and 10
if number > 0:  # If the number is greater than 0
    print(f"{number} is positive")  # Print that the number is positive
elif number == 0:  # If the number is exactly 0
    print(f"{number} is zero")  # Print that the number is zero
else:  # If the number is less than 0
    print(f"{number} is negative")  # Print that the number is negative

