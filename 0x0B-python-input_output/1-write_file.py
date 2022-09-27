#!/usr/bin/python3
"""Defines a function read_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file"""

    with open(filename = "", mode = "w", encoding = "UTF-8") as myFile:
        myFile.write(text)
