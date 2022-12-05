#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix is None):
        return
    for rows in matrix:
        for col in rows:
            print('{:d} '.format(col), end='')
        print('')
