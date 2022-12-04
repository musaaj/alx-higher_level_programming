#!/usr/bin/python3
import add_0 as add


def main():
    a = 1
    b = 2

    print("<a {0}> + <b {1}> = <add(a, b) {2}>".format(a, b, add.add(a, b)))


if (__name__ == "__main__"):
    main()
