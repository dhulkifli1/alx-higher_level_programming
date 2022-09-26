#!/usr/bin/python3
"""Defines an attribute and object lookup function"""


def lookup(obj):
    """Returns a list of all the available attributes and methods"""

    return dir(obj)
