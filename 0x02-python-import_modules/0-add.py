#!/usr/bin/python3
if (__name__ == "__main__"):
    import add_0 as d

    def main():
        """The entry of our program
        """
        a = 1
        b = 2
        print("{0:d} + {1:d} = {2:d}".format(a, b, d.add(a, b)))
    main()
