#!/usr/bin/python3
"""
Function that describe perimeter of island
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in hte grid.

    Args:
        grid: List of list of integers
    Returns:
        Perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                """ Add 4 sides for each land cell."""
                perimeter += 4

                """ Suntract 2 for each adjacent land cell (above)"""
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

                """ Subtract 2 for each adjacent land cell (left)."""
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
