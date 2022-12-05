#!/usr/bin/python3
def multiple_returns(sentence):
    first_chr = None
    if ((sentence is not None) and (len(sentence) > 0)):
        return (len(sentence), sentence[0])
    return (0, first_chr)
