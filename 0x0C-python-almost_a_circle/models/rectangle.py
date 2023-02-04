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
        self.__y = value
