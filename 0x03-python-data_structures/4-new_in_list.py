#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (my_list is None):
        return (None)
    tmp = [item for item in my_list]
    if ((idx < 0) or (idx >= len(my_list))):
        return (tmp)
    tmp[idx] = element
    return (tmp)
