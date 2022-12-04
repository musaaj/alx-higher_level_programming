#!/usr/bin/python3

if (__name__ == '__main__'):
    from sys import argv

    arg_len = len(argv)
    i: int = 1
    result: int = 0

    while (i < arg_len):
        result += int(argv[i])
        i += 1
    print('{:d}'.format(result))
