#!/usr/bin/python3
"""save object to file"""
import json


def save_to_json_file(my_obj, filename):
    """save python object to file

    Args:
        my_obj: any
        filename: string

    Return: none
    """
    with open(filename, 'w') as fp:
        return json.dump(my_obj, fp)
