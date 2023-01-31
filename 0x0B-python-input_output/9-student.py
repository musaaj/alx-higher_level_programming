#!/usr/bin/python3
"""
Student module
"""


class Student:
    """
    A simple student class
    """

    def __init__(self, first_name, last_name, age):
        """constructor method

        Args:
            first_name: str
            last_name str
            age: int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get dictionary reps of all fields of
        instance of this class
        """
        return vars(self)
