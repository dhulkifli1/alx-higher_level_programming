#!/usr/bin/python3
"""Define a Square class"""

class Square:
    """Defines a square"""

    def __init__(self, size):
        """Add size of the square as private instance variable

        Parameters:
            size (int): size of the square
        """

        self.__size = size
