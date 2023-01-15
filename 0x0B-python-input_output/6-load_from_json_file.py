#!/usr/bin/python3
"""json to object"""
import json


def load_from_json_file(filename):
    """json file to python object

    Args:
        filename: string

    Return: any
    """
    with open(filename, 'r') as fp:
        return json.load(fp)
