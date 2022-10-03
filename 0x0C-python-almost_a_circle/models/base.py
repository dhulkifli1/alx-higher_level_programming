#!/usr/bin/python3
"""Contains a Base class"""
import json


class Base:
    """Represents a Base class"""

    __nb_objects = 0
    def __init__(self, id=None):
        """Class constructor"""

        if id != None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        new_list = []
        for obj in list_objs:
            new_list.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            json.dump(new_list, f)
