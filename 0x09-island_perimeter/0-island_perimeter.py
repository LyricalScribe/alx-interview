#!/usr/bin/python3
"""Calculate island perimeter"""


def island_perimeter(grid):
    """Calculate perimeter"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                # Check left
                if j != 0:
                    if grid[i][j - 1] == 0:
                        perimeter += 1
                # Check right
                if j < cols - 1:
                    if grid[i][j + 1] == 0:
                        perimeter += 1
                # Check up
                if i != 0:
                    if grid[i - 1][j] == 0:
                        perimeter += 1
                # Check down
                if i < rows - 1:
                    if grid[i + 1][j] == 0:
                        perimeter += 1

    return perimeter
