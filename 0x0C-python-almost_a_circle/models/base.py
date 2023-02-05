#!/usr/bin/python3
"""main base class"""
import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor

        Args:
            id: int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """get json reps of a list of dictionaries"""
        if not list_dictionaries or not len(list_dictionaries):
            return '[]'
        return json.dumps(list_dictionaries)
