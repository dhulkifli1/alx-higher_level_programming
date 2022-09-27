#!/usr/bin/python3
"""Defines a function read_file"""


def append_write(filename="", text=""):
    """Writes a string to a text file

    Params:
        filename (str): name of file
        text (str): text to be written in the file

    Return:
        Number of characters written in the file
    """

    with open(filename, "a", encoding = "UTF-8") as myFile:
        return myFile.write(text)
