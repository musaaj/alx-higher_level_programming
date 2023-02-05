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

    def __str__(self):
        """str method"""
        rectangle_str = '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                                self.__x,
                                                                self.__y,
                                                                self.__width,
                                                                self.__height
                                                                )
        return rectangle_str

    def area(self):
        """get area of this rectangle"""
        return self.__width * self.__height

    def display(self):
        """print this rectangle"""
        for i in range(self.__y):
            print('')
        for i in range(self.__height):
            print('{}{}'.format(' ' * self.__x, '#' * self.__width))

    def update(self, *args, **kwargs):
        """update fields of this objects

        Args:
            args: variable list arguments
            *kwargs: variable key-value arguments
        """
        args_len = len(args)
        if not args_len:
            if kwargs.get('id', ''):
                self.id = kwargs.get('id')
            if kwargs.get('width', ''):
                self.__width = kwargs.get('width')
            if kwargs.get('height', ''):
                self.__height = kwargs.get('height')
            if kwargs.get('x', ''):
                self.__x = kwargs.get('x')
            if kwargs.get('y', ''):
                self.__y = kwargs.get('y')
        if args_len:
            self.id = args[0]
        if args_len > 1:
            self.__width = args[1]
        if args_len > 2:
            self.__height = args[2]
        if args_len > 3:
            self.__x = args[3]
        if args_len > 4:
            self.__y = args[4]

    def to_dictionary(self):
        """get dictionary representation of this object"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
