#!/usr/bin/python3
"""Lookup module"""


def lookup(obj):
    """check for object attributes

    Args:
        obj: any

    Return: list of @obj attributes
    """
    return dir(obj)
