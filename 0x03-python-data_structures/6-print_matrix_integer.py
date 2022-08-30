#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            print("{:d}".format(matrix[x][y]),
                    end=" " if y < len(matrix[0]) - 1 else '\n')
