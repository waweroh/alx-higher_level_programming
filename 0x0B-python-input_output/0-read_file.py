#!/usr/bin/python3
"""Defines a function that reads files and print result to stdout"""


def read_file(filename=""):
        """Reads a text file and prints it to the stdout"""
            with open(filename, mode="r", encoding="utf-8") as a_file:
                        print(a_file.read(), end="")
