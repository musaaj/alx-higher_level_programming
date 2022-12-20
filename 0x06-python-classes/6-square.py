#!/usr/bin/python3

"""Simple python module that does
absolutely nothing

This is just another paragraph
"""


class Square(object):
    """Class declaration example

    Simple class docstring sample
    """

    def __init__(self, size=0, position=(0, 0)):
        """constructor method of our class

    This function initiate our class instance

         Args:
            size (int): size of our square object
            position (tuple): position of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self, value):
        """Getter for position

        Returns:
            tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position

        Args:
            value (tuple): must be a tuple of 2 integers
        """
        if tupe(value) != tuple\
                or len(value) != 2\
                or type(value[0]) != int\
                or type(value[1]) != int\
                or value[0] < 0\
                or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints square to stdout

        just prints square
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            if self.__position[1] == 0:
                print(' ' * self.__position[0], end='')
            print('#' * self.__size)
