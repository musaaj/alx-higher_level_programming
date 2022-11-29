#!/usr/bin/python3
chars = ""

for c in range(ord('a'), ord('{')):
    if ((chr(c) != 'q') and (chr(c) != 'e')):
        chars += chr(c)
print(chars, end='')
