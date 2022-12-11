#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    my_dict = dict(sorted(a_dictionary.items()))
    for key in my_dict:
        print("{0}: {1}".format(key, my_dict[key]))
