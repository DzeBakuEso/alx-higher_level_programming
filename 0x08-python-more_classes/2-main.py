#!/usr/bin/python3
"""
This script tests the Rectangle class.
"""
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(
    my_rectangle.area(), my_rectangle.perimeter()
))
print("--")
my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(
    my_rectangle.area(), my_rectangle.perimeter()
))
