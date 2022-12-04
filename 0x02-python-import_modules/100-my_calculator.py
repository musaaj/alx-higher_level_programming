#!/usr/bin/python3

if (__name__ == '__main__'):
    from sys import argv
    from calculator_1 import add, sub, mul, div

    funcs = [add, sub, mul, div]
    operators = "+-*/"
    arg_len = len(argv)
    op: str = ""

    if (arg_len != 4):
        print('Usage: {} <a> '
              '<operator> <b>'.format(argv[0]))
        exit(1)

    op_index = operators.find(argv[2])
    if (op_index == -1):
        print('Unknown operator. '
              'Available operators are +, -, * and /')
        exit()

    print('{:d} {:s} {:d} = {:d}'.format(
        int(argv[1]),
        argv[2],
        int(argv[3]),
        funcs[op_index](int(argv[1]), int(argv[3]))))
