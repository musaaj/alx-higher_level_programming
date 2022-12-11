#!/usr/bin/python3

def best_score(a_dictionary):
    best_key = None
    best_score = 0

    if (a_dictionary is None):
        return None
    if (len(a_dictionary) == 0):
        return None
    for (key, value) in a_dictionary.items():
        if (value > best_score):
            best_key = key
            best_score = value
    return (best_key)
