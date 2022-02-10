#!/usr/bin/python3
"""
The 0-lookup module supplies one function, lookup(). For example,
lookup(MyClass1)
"""


def lookup(obj):
        """returns list of available attributes and methods of an object"""
        return dir(obj)
