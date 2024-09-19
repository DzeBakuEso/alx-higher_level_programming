#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    This function squares all integers in the input 2D matrix.
    A new matrix is returned without modifying the input matrix.
    """
    # Use list comprehension to create a new matrix with squared values
    return [[x ** 2 for x in row] for row in matrix]
