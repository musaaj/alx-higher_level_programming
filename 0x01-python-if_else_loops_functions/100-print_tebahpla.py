#!/usr/bin/python3
toggle: bool = False
for c in range(ord('z'), 96, -1):
    if (toggle):
        c = c - 32
        toggle = False
    else:
        toggle = True
    print("{0}".format(chr(c)), end="")
