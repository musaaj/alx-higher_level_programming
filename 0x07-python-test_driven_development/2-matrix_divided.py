#!/usr/bin/python3
'''module matrix does matrix related operations

The module is super simple
'''


def matrix_divided(matrix, div):
    '''divide a matrix by a giving scalar

    Args:
        matrix: list of lists of int/floats of equal length
        div: int or floats

    Returns: list of lists of int/floats of equal length
    '''
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix'
                        ' (list of lists) of integers/floats')
    if not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix'
                        ' (list of lists) of integers/floats')
    length = len(matrix[0])
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError('matrix must be a matrix'
                            ' (list of lists) of integers/floats')
        for j in i:
            if type(j) not in [int, float]:  # check each item
                raise TypeError('matrix must be a matrix'
                                ' (list of lists) of integers/floats')
        if len(i) != length:
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(col / div, 2) for col in row] for row in matrix]
