#!/usr/python3

"""This module defines a function to generate Pascal's triangle."""

def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n.

    Args:
        n (int): The number of rows for Pascal's triangle.

    Returns:
        list: A list of lists where each inner list represents a row
              of Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])  # Sum of elements from the previous row
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle
