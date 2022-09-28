#!/usr/bin/python3
"""Defines a class Square"""
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size):
        """Constructor method for Square class"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
