#!/usr/bin/python3
"""Simple python3 module for practice

It is super simple
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
