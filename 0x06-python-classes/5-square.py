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

    @property
    def size(self):
        """Getter method for self.__size private variable"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for self.__size private variable"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current square area"""

        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character #"""

        if self.__size == 0:
            print("")
        for height in range(self.__size):
            for width in range(self.__size):
                print("#", end = "")
            print("")
