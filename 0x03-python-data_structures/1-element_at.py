#!/usr/bin/python3
def element_at(my_list, idx):
    """element_at(my_list) gets an element of a list
    object at a specific index
    Args:
        my_list (list): list of containing any data type
        idx (int): index of item in my_list to get
    Return:
        item at index idx if withing the range
        else None
        if idx < 0 None
        if my_list is None None
    """
    if (idx < 0):
        return (None)
    if (idx >= len(my_list)):
        return (None)
    if (my_list is None):
        return (None)
    return (my_list[idx])
