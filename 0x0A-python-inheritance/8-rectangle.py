#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """Represents the BaseGeometry class"""

    def __init__(self):
        """Instantiation for BaseGeometry class"""

        pass

    def area(self):
        """Represents area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks whether value is an int and is >= 0"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
