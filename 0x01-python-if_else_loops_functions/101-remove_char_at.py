#!/usr/bin/python3

def remove_char_at(str, n):
    i: int = 0
    tmp: str = ""
    strl: int = len(str)

    while(i < strl):
        if (i != n):
            tmp += str[i]
        i += 1
    print(tmp)
