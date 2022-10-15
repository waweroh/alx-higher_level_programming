#!/usr/bin/python3
"""
This module 0-add_integer suppliesthe function add_integer()
returning sum of int type only
"""


def add_integer(a, b=98):
    """ Returns the addition of a and b, an exact integer."""

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile(tests/0-add_integer.txt)
