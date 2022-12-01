#!/usr/bin/python3
for c in range(ord('a'), ord('{')):
    if ((chr(c) != 'q') and (chr(c) != 'e')):
        print("{0}".format(chr(c)), end='')
