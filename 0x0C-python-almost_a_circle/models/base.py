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

    @classmethod
    def save_to_file(cls, list_objs):
        """save list of objects to file"""
        json_of_obj_list = '[]'
        if list_objs:
            json_of_obj_list = cls.to_json_string(
                        [object.to_dictionary() for object in list_objs]
                    )
        filename = '{}.json'.format(cls.__name__)
        with open(filename, 'w') as fp:
            fp.write(json_of_obj_list)
            fp.close()

    @staticmethod
    def from_json_string(json_string):
        """string to objects"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create object of type"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

