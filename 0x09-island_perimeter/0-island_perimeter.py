#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
Calculate perimeter of the island
"""
__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-04"
__version__ = "1.0"


def island_perimeter(grid):
    """
    Calculate the perimeter of an island described in a grid.

    Args:
        grid (list of list of ints): A 2D list representing the grid.
                                     0 -> water, 1 -> land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for the land cell
                perimeter += 4
                # Check the top cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                # Check the left cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 12
