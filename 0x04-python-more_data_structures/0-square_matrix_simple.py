#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use a list comprehension to create a new matrix with squared values
    return[[x ** 2 for x in row] for row in matrix]
