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
        square_str = '[Square] ({}) {}/{} - {}'.format(self.id,
                                                        self.x,
                                                        self.y,
                                                        self.width
                                                        )
        return square_str

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
        super().update(*args, **kwargs)
