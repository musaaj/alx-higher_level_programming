#!/usr/bin/python3
def max_integer(my_list=[]):
    my_max = 0
    if ((my_list is None) or (len(my_list) == 0)):
        return (None)
    for i in my_list:
        my_max = i if i > my_max
    return (i)