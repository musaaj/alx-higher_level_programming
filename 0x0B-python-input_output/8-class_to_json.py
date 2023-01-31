#!/usr/bin/python3
"""
Object to json
"""


def class_to_json(obj):
    """returns dictionary reps of an object fields

    Args:
        obj: any none primitive object

    Return: dict, dictionary reps of @obj
    """
    return vars(obj)
