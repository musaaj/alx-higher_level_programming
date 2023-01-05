#!/usr/bin/python3
'''Module to print pretty square

Just super simple
'''


def print_square(size):
    '''Prints beautiful square

    Args:
        size: integer
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
