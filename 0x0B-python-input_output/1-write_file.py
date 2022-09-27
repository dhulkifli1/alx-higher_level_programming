#!/usr/bin/python3
"""Defines a function read_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file"""

    with open(filename, "w", encoding = "UTF-8") as myFile:
        return myFile.write(text)
