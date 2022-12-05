#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for matrice in matrix:
        for i in matrice:
            print('{:d} '.format(i), end='')
        print('')
