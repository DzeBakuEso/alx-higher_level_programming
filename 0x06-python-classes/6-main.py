#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()  # Should print a 3x3 square

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()  # Should print a 3x3 square with a position of (1, 1)

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()  # Should print a 3x3 square with a position of (3, 0)

print("--")
