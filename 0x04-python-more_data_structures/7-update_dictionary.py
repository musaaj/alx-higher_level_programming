#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    tmp = dict(a_dictionary.items())
    tmp[key] = value
    return tmp
