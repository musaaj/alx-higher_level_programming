#!/usr/bin/python3

def search_replace(my_list, search, replace):
    result = [replace for i in my_list if i == search else i]
    return result
