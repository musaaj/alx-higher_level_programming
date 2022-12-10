#!/usr/bin/python3

def search_replace(my_list, search, replace):
    result = [i for i in my_list if i != search]
    return result
