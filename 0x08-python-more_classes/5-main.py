#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
                                        my_rectangle.perimeter()))

# Deleting the rectangle instance
del my_rectangle

# Try accessing the deleted instance and handle the resulting exception
try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
