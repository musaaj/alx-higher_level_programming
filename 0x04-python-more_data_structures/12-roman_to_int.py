#!/usr/bin/python3

def tokenize(roman_string=""):
    token: str = ""
    tokens: str = []
    size: int = len(roman_string)
    i: int = 0

    while (i < size):
        if (roman_string[i] == "I"):
            token += "I"
            if (roman_string[i + 1] == "V"):
                token += "V"
                i += 1
            elif (roman_string[i + 1] == "X"):
                token += "X"
                i += 1
        elif (roman_string[i] == "V"):
            token += "V"
        elif (roman_string[i] == "X"):
            token += "X"
            if (roman_string[i + 1] == "C"):
                token += "C"
                i += 1
            elif (roman_string[i + 1] == "L"):
                token += "L"
                i += 1
        elif (roman_string[i] == "L"):
            token += "L"
        elif (roman_string[i] == "C"):
            token += "C"
            if (roman_string[i + 1] == "D"):
                token += "D"
                i += 1
            elif (roman_string[i + 1] == "M"):
                token += "M"
                i += 1
        elif (roman_string[i] == "D"):
            token += "D"
        elif (roman_string[i] == "M"):
            token += "M"
        if(token):
            tokens.append(token)
        token = ""
        i += 1
    return tokens


def to_int(roman_token=""):
    if (roman_token == "I"):
        return 1
    if (roman_token == "IV"):
        return 4
    if(roman_token == "V"):
        return 5
    if (roman_token == "IX"):
        return 9
    if (roman_token == "X"):
        return 10
    if (roman_token == "XL"):
        return 40
    if (roman_token == "XC"):
        return 90
    if (roman_token == "L"):
        return 50
    if (roman_token == "C"):
        return 100
    if (roman_token == "CD"):
        return 400
    if (roman_token == "D"):
        return 500
    if (roman_token == "CM"):
        return 900
    if (roman_token == "M"):
        return 1000
    return 0


def roman_to_int(roman_string):
    if (roman_string is None or type(roman_string) is not str):
        return 0
    roman_string += " "
    tokens = tokenize(roman_string)
    arabic_tokens = [to_int(i) for i in tokens]
    return sum(arabic_tokens)
