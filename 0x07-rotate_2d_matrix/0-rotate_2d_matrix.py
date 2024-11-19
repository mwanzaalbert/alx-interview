#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
0-rotate_2d_matrix.py

This module provides a function to rotate a square 2D matrix
90 degrees clockwise in place.

The function `rotate_2d_matrix` accepts a non-empty
n x n matrix, modifies it directly, and ensures the
rotation operation is performed efficiently.

Usage Example:
--------------
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
    # Output:
    # [
    #     [7, 4, 1],
    #     [8, 5, 2],
    #     [9, 6, 3]
    # ]

The module assumes that:
- The input matrix is non-empty.
- The matrix is always a square (n x n).
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list[list[int]]): 2D matrix to be rotated.
    """
    n = len(matrix)

    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to get the rotated matrix
    for row in matrix:
        row.reverse()


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
