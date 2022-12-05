#!/usr/bin/python3
def no_c(my_string):
    tmp: str = ''
    for c in my_string:
        if ((c != 'c') and (c != 'C')):
            tmp += c
    return (tmp)
