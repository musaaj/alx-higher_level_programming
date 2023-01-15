#!/usr/bin/python3
"""Read text file"""


def read_file(filename=""):
    """Read and print text file to stdout

    Args:
        filename: string
    """
    with open(filename, 'r') as fp:
        for line in fp:
            print('{}'.format(line), end='')
