#!/usr/bin/python3
"""Define a Square"""

class Square:
    """Defines a Square class"""

    def __init__(self, size=0):
        """Ensures size is an int and is greater than 0

        Parameters:
            size (int): size of the square
        """

        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
