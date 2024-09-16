#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements by using tuple unpacking with default values
    a1, a2 = (tuple_a + (0, 0))[:2]
    b1, b2 = (tuple_b + (0, 0))[:2]
    
    # Return the tuple with the sum of corresponding elements
    return (a1 + b1, a2 + b2)
