#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = number % -10
else:
    digit = number % 10
    if digit > 5:
        print("Last digit of {:d} is {:d} and is greater than 5".forma        t
              (number, digit))
    elif digit % 10 == 0:
        print("Last digit of {:d} is {:d} and is 0".format(number, dig        i
                                                           t))
    else:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0        "
              .format(number, digit))
