#!/usr/bin/python3
"""Defines a function is_same_class"""


def is_same_class(obj, a_class):
    """Returns whether an object is an instance of a class"""

    if type(obj) == a_class:
        return True
    return False
