#!/usr/bin/python3
"""
Function that returns a list of integers representing the Pascal's Triangle
"""


def pascal_triangle(n):
    """
    pascal triangle function
    """

    if n <= 0:
        return []
    tri = []

    for row in range(n):
        new_tri = []

        for index in range(row + 1):
            if index == 0 or index == row:
                new_tri.append(1)
            else:
                prev_value = tri[row - 1]
                new_value = prev_value[index - 1] + prev_value[index]
                new_tri.append(new_value)

        tri.append(new_tri)
    return tri
