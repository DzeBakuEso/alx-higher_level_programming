#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate over each row in the matrix
    for row in matrix:
        # Print each element in the row, using str.format() for formatting
        print(" ".join("{:d}".format(num) for num in row))
