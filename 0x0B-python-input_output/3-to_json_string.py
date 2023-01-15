#!/usr/bin/python3
"""object to string"""
import json


def to_json_string(my_obj):
    """object to json

    Args:
        my_obj: any

    Return: string
    """
    return json.dumps(my_obj)
