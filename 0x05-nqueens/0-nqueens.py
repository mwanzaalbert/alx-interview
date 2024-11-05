#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
nqueens - Solves the N Queens puzzle.

The N Queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. This module uses a backtracking approach to find
all possible solutions to the problem.

Usage:
    nqueens N
    - N: The size of the board (must be an integer greater or equal to 4).

The program validates the input and prints each solution as a list of
coordinates, where each inner list [i, j] represents a queen placed in
row i and column j.

Example:
    $ ./0-nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]
"""

import sys
from typing import List


def print_solutions(n, solutions):
    # type: (int, List[List[int]]) -> None
    """
    Prints each solution in the required format, where each solution
    is represented as a list of [row, col] pairs indicating the queen's
    position on the board.

    Args:
        n (int): The size of the chessboard.
        solutions (list of list of int): All solutions found, where each
            solution is a list of column indices for queen positions in
            each row.
    """
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


def is_safe(board, row, col):
    # type: (List[int], int, int) -> bool
    """
    Determines if placing a queen on the board at the given row and column
    is safe, meaning it will not be attacked by any other queens.

    Args:
        board (list of int): The current board setup where board[i] is the
                             column of the queen in row i.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if it is safe to place a queen at (row, col),
              False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    # type: (int) -> List[List[int]]
    """
    Solves the N Queens problem using backtracking to find all possible
    configurations of N non-attacking queens on an N×N board.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list of list of int: A list of all solutions, where each solution
            is a list of column indices for queen positions in each row.
    """
    solutions = []  # type: List[List[int]]
    board = [-1] * n  # type: List[int]

    def backtrack(row):
        # type: (int) -> None
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Find and print all solutions for N Queens
    solutions = solve_nqueens(N)
    print_solutions(N, solutions)
