#!/usr/bin/python3

"""Simple python module that does
absolutely nothing

This is just another paragraph
"""


class Square:
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
        if isinstance(position, tuple) is False\
                or len(position) != 2\
                or isinstance(position[0], int) is False\
                or isinstance(position[1], int) is False\
                or position[0] < 0\
                or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
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
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
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
        if isinstance(value, tuple) is False\
                or len(value) != 2\
                or isinstance(value[0], int) is False\
                or isinstance(value[1], int) is False\
                or value[0] < 0\
                or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints square to stdout

        just prints square
        """
        print()
        if self.__size == 0:
            return
        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
