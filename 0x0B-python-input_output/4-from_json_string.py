#!/usr/bin/python3
"""json to object"""
import json


def from_json_string(my_str):
    """json to python obj

    Args:
        my_str: string

    Return: any
    """
    return json.loads(my_str)
