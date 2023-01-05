#!/usr/bin/python3
"""
Simple python3 module for practice

>>> add_integer(2, 3)
5
>>> add_integer(3, 4.3)
7
>>> add_integer(None, 3)
Traceback (most recent call last):
    ...
TypeError: a must be an integer
>>> add_integer(100, '39')
Traceback (most recent call last):
    ...
TypeError: b must be an integer
>>> add_integer([2], 9)
Traceback (most recent call last):
    ...
TypeError: a must be an integer
"""


def add_integer(a, b=98):
    """
    Add two integers

    Args:
        a: int
        b: int

    Returns: int sum of @a and @b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
