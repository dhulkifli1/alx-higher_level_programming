#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix)):
            print("{}".format(matrix[x][y]), end = " " if y < len(matrix) - 1 else '\n')
