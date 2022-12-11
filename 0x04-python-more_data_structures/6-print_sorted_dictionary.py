#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    my_dict = dict(sorted(a_dictionary.items()))
    for key, item in my_dict:
        print("{0}: {1}".format(key, item))
