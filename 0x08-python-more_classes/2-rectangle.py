#!/usr/bin/python3
"""Simple Module

The triangle module is just for practice
"""


class Rectangle:
    """Simple Rectangle class"""

    def __init__(self, width=0, height=0):
        """constructor method

        Args:
            width: must be an unsigned int
            height: must be an unsigned int
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self._width = width
        self._height = height

    @property
    def width(self):
        """width getter

        Return: unsigned int
        """
        return self._width

    @property
    def height(self):
        """height getter

        Return: unsigned int
        """
        return self._height

    @width.setter
    def width(self, value):
        """width setter

        Args:
            value: unsigned int
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @height.setter
    def height(self, value):
        """height getter

        Args:
            value: unsigned int
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

    def area(self):
        """find area of a rectangle instance

        Return: unsigned int
        """
        if self._width == 0 or self._height == 0:
            return 0
        return self._width * self._height

    def perimeter(self):
        """find perimeter of a rectangle instance

        Return: unsigned int
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * self._width + 2 * self._height
