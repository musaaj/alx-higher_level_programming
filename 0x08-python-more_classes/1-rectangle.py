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
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.width = width
        self.height = height

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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value
