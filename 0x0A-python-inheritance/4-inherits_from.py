#!/usr/bin/python3
"""Defines a function inherits_from"""


def inherits_from(obj, a_class):
    """Shows whether an object inherited from a specified class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
