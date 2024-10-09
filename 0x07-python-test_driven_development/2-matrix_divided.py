#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    This defines a function that divides all elements of a matrix by div.
    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The divisor.
    Returns:
        list: A new matrix with each element divided by div
              rounded to 2 decimal places.
    Raises:
        TypeError: If the matrix is not a matrix (list of lists)
                    of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Check if all elements in the matrix are either int or float
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

    # Check if each row of the matrix is of the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with each element divided by div
    return [[round(elem / div, 2) for elem in row] for row in matrix]
