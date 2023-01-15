#!/usr/bin/python3
"""write or append to text file"""


def append_write(filename="", text=""):
    """write or append text file

    Args:
        filename: string
        text: string

    Return: int number of char written
    """
    with open(filename, 'a') as fp:
        return fp.write(text)
