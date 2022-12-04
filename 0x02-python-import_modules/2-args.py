#!/usr/bin/python3

if (__name__ == '__main__'):
    from sys import argv

    arg_len = len(argv)
    info = 'argument'
    i: int = 1

    if (arg_len < 2):
        info += 's.'
    if (arg_len == 2):
        info += ':'
    if (arg_len > 2):
        info += 's:'
    print('{:d} {:s}'.format(arg_len - i, info))
    while (i < arg_len):
        print('{:d}: {:s}'.format(i, argv[i]))
        i += 1
