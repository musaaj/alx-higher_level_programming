#!/usr/bin/python3
import random


def to_positive(n):
    if (n < 0):
        return (n * -1)
    return (n)


number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
if (number < 0):
    last_digit *= -1
if ((to_positive(last_digit) < 6) and (to_positive(last_digit) != 0)):
    print(f"Last digit of {number:d} is {last_digit} and is less than "
          "6 and not 0")
elif (to_positive(last_digit) > 5):
    print(f"Last digit of {number: d} is {last_digit:d} "
          "and is greater than 5")
elif (last_digit == 0):
    print(f"Last digit of {number:d} is {last_digit:d} "
          "and is 0")
