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

    def to_json(self, attrs=None):
        """get dictionary reps of all fields of
        instance of this class

        Args:
            attrs: list of strings

        Return: dictionary reps of self
        """
        if attrs is None:
            return vars(self)
        object_attrs = {}
        attributes = vars(self)
        for field in attrs:
            if field in attributes:
                object_attrs[field] = attributes[field]
        return object_attrs

    def reload_from_json(self, json):
        """replace self attributes

        Args:
            json: dictionary
        """
        for key in json:
            if self.__getattribute__(key):
                self.__setattr__(key, json[key])
