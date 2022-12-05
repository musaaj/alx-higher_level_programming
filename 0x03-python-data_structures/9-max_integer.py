#!/usr/bin/python3
import sys


def max_integer(my_list=[]):
    my_max = -sys.maxint - 1
    if ((my_list is None) or (len(my_list) == 0)):
        return (None)
    for i in my_list:
        my_max = i if i > my_max else my_max
    return (i)
