#!/usr/bin/python3
'''Format and print text in readable format

Just simple demo
'''


def text_indentation(text):
    '''Print long text in readable format

    Args:
        text: string
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    skip = False
    for i in text:
        if i in '.?:':
            print('{}\n'.format(i))
            skip = True
        elif skip and i in ' \t':
            pass
        else:
            print(i, end='')
            skip = False
