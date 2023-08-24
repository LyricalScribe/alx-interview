#!/usr/bin/python3
"""
Rotates 2D Matrix
90 degrees clockwise
"""

def rotate_2d_matrix(matrix):
    """Transposing matrix"""

    rows = len(matrix)

    for row in range(rows):
        for col in range(row, rows):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in matrix:
        row.reverse()
