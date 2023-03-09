#!/usr/bin/python3
"""Contains function text_indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines
    after each of these characters: . ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        for character in text:
            if character not in ['.', '?', ':']:
                print(character, end="")
            else:
                print(character)
                print("")
