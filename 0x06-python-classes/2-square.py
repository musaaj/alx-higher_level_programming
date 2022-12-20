#!/usr/bin/python3

"""Simple python module that does
absolutely nothing

This is just another paragraph
"""


class Square(object):
    """Class declaration example

    Simple class docstring sample
    """

    def __init__(self, size=0):
        """constructor method of our class

    This function initiate our class instance

         Args:
            size (int): size of our square object
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
