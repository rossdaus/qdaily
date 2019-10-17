#!/usr/bin/env python3
matrix = """
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""

# create 2d array of ints from matrix string
matrix = matrix.strip().split("\n")
matrix = [[int(char) for char in row if char.isdigit()] for row in matrix]

def walk(matrix, x, y):
    """Seek adjoining land, set to 0 to avoid rediscovery."""
    print("found land", x, y)
    matrix[y][x] = 0

    if y > 0 and matrix[y - 1][x]:
        walk(matrix, x, y - 1)
    if x > 0 and matrix[y][x - 1]:
        walk(matrix, x - 1, y)
    if y < len(matrix) - 1 and matrix[y + 1][x]:
        walk(matrix, x, y + 1)
    if x < len(matrix[0]) - 1 and matrix[y][x + 1]:
        walk(matrix, x + 1, y)

    return 1


def count_islands(matrix):
    """Count number of islands for a 2d array of 1s and 0s."""
    islands = 0

    for y, row in enumerate(matrix):
        for x, item in enumerate(row):

            if matrix[y][x] == 1:
                islands += walk(matrix, x, y)
                print("==============")

    return islands

print(count_islands(matrix), "islands found")