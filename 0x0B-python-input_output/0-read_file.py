#!/usr/bin/python3
"""Defines a function read_file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout

    Params:
        filename (str): name of the file
    """

    with open(filename, encoding = "UTF-8") as myFile:
        print(myFile.read(), end = "")
