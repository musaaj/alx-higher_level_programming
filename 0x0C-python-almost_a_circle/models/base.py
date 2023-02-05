#!/usr/bin/python3
"""main base class"""
import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """load objects from file"""
        try:
            with open(f'{cls.__name__}.json', 'r') as fp:
                objects_dict = cls.from_json_string(fp.read())
                fp.close()
            return [cls.create(**item) for item in objects_dict]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize and save objects to csv file"""
        csv_contents = []
        with open(f'{cls.__name__}.csv', 'w') as fp:
            if list_objs:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        csv_contents.append(
                                    [
                                      obj.id,
                                      obj.width,
                                      obj.height,
                                      obj.x,
                                      obj.y
                                    ]
                                )
                    if cls.__name__ == 'Square':
                        csv_contents.append(
                                    [
                                      obj.id,
                                      obj.size,
                                      obj.x,
                                      obj.y
                                    ]
                                )
            writer = csv.writer(fp)
            for row in csv_contents:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """load objects from csv file"""
        list_objs = []
        try:
            with open(f'{cls.__name__}.csv', 'r', newline='') as fp:
                reader = csv.reader(fp)
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        obj = cls(1, 1)
                        obj.update(*[int(i) for i in row])
                        list_objs.append(obj)
                    if cls.__name__ == 'Square':
                        obj = cls(1)
                        obj.update(*[int(i) for i in row])
                        list_objs.append(obj)
            return list_objs
        except FileNotFoundError:
            return []
