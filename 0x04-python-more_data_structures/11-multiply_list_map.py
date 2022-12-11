#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    tmp = list(map(my_list, lambda x: x * number))
    return tmp
