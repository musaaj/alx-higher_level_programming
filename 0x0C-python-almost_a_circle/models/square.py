#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor

        Args:
            size: int
            x: int
            y: int
            id: int
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """get string representation of this"""
        return '[Square] ({}) {}/{} - {}'.format(
                self.id,
                self.x,
                self.y,
                self.width)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update my fields"""
        args_len = len(args)
        if not args_len:
            if kwargs.get('id', ''):
                self.id = kwargs.get('id')
            if kwargs.get('size', ''):
                self.size = kwargs.get('size')
            if kwargs.get('x', ''):
                self.x = kwargs.get('x')
            if kwargs.get('y', ''):
                self.y = kwargs.get('y')
        if args_len:
            self.id = args[0]
        if args_len > 1:
            self.size = args[1]
        if args_len > 2:
            self.x = args[2]
        if args_len > 3:
            self.y = args[3]

    def to_dictionary(self):
        """get the dictionary representation of this object"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
