#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Do not return anything. The matrix must be edited in-place"""
    transposed_matrix = [[0 for _ in range(len(matrix))]
                         for _ in range(len(matrix[0]))]
    for col in range(len(matrix)):
        for row in range(len(matrix[0])):
            transposed_matrix[col][row] = matrix[row][col]

    matrix.clear()
    for row in transposed_matrix:
        row.reverse()
    matrix.extend(transposed_matrix)


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
