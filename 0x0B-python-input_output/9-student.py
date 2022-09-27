#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Defines a Student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation method for Student instances"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""

        return obj.__dict__
