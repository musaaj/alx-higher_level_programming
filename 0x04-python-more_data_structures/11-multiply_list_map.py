#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    tmp = dict(map(my_list.items(), lambda key, val: (key, val * number)))
    return tmp
