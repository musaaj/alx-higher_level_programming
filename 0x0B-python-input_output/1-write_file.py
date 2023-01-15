#!/usr/bin/python3
"""Write string to file"""


def write_file(filename="", text=""):
    """write a string to file

    Args:
        filename: string
        text: string
    """
    with open(filename, 'w') as fp:
        return fp.write(text)
