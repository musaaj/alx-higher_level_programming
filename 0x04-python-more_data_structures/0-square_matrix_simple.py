#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = [[col**2 for col in row] for row in matrix]
    return result
