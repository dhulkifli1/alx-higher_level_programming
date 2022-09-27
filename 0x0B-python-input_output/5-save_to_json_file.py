#!/usr/bin/python3
"""Defines a function save_to_json_file"""


import json
def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""

    with open(filename, 'w', encoding = 'UTF-8') as myFile:
        myJsonObj = json.dumps(my_obj)
        myFile.write(myJsonObj)
