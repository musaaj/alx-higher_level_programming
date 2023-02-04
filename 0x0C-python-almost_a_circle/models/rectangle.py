#!/usr/bin/python3
"""Rectangle Module"""
import models.base


class Rectangle(models.base.Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor

        Args:
            width: int
            height: int
            x: int
            y: int
            id: int
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter for width

        Return: int
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width

        Args:
            value: int
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """getter for height

        Return: int
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height

        Args:
            value: int
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """getter for x

        Return: int
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x

        Args:
            value: int
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """getter for y

        Return: int
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y

        Args:
            value: int
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
