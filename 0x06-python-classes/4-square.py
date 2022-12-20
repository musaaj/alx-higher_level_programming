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

    def area(self):
        """find area of a square instance

        Calculate the area of the square instance

        Returns:
            int: The area of the square
        """
        return self.__size**2

    @property
    def size(self):
        """our size getter

        Returns:
            int: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter method for size

        Args:
            value int: must be an integer >= 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
