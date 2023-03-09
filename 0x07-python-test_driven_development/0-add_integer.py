#!/usr/bin/python3
"""Contains function add_integer"""


def add_integer(a, b=98):
    """Adds 2 integers"""
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    elif type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    else:
        if type(a) == "float":
            a = int(a)
        elif type(b) == "float":
            b = int(b)
        else:
            return int(a + b)
