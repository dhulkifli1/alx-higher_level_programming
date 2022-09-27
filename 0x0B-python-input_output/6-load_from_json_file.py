#!/usr/bin/python3
"""Defines a function load_from_json_file"""


import json
def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""

    with open(filename, 'r', encoding = 'UTF-8') as myFile:
        json_object = json.load(myFile)
        return json_object
