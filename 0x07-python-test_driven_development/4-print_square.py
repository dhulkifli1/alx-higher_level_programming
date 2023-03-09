#!/usr/bin/python3
"""Contains function print_square"""


def print_square(size):
    """Prints a square with the character #"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for _ in range(size):
            for _ in range(size):
                print("#", end="")
            print("")
