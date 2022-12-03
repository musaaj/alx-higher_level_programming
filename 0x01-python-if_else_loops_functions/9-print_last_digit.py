#!/usr/bin/python3

def print_last_digit(number):
    last_digit: int = int(str(number)[-1])
    print("{0}".format(last_digit), end="")
    return (last_digit)
