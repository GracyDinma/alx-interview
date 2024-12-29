#!/usr/bin/python3
"""
Pascal triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's
    triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        """ Create the next row based on the previous row."""
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
