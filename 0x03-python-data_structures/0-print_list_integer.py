#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """print_list_integer(mylist)
    prints all items in a list of integers
    Args:
        my_list: must be a list containing only ints
    Return:
        None
    """
    for item in my_list:
        print('{:d}'.format(item))
