#!/usr/bin/python3
"""Defines a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size):
        """Constructor method for Square class"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """String method for Square class"""

        return "[Square] {}/{}".format(self.__size, self.__size)
