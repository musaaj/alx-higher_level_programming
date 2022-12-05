#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (my_list is None):
        return (my_list)
    if ((idx < 0) or (idx >= len(element))):
        return (my_list)
    tmp = [item for item in my_list]
    tmp[idx] = element
    return (tmp)

