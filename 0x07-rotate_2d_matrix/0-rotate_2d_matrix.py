#!/usr/bin/python3
"""
2D matrix that rotate 90 degree clockwise in-place
"""
class PrintableMatrix(list):
    """
    Custom list class to modify the print behavior of the entire matrix.
    """
    def __repr__(self):
        return "\n".join(str(row) for row in self)


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in place.
    """
    n = len(matrix)

    """ Transpose the matrix."""
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    """ Reverse each row."""
    for row in matrix:
        row.reverse()

    # Print each row of the rotated matrix
    for row in matrix:
        print(row)
