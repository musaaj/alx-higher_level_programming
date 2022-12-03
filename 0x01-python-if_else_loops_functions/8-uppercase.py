#!/usr/bin/python3

def uppercase(str):
    tmp: str = ""
    code: int = 32
    for c in str:
        if ((ord(c) >= ord('a')) and (ord(c) <= ord('z'))):
            tmp += chr(ord(c) - code)
        else:
            tmp += c
    print("{0}".format(tmp))
