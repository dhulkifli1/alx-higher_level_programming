#!/usr/bin/python3
"""Defines a function load_from_json_file"""


import json
def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""

    with open(filename, 'w', encoding = 'UTF-8') as myFile:
        for element in myFile:
            x = json.loads(element)
        return x
