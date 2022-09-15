#!/usr/bin/python3
"""Define a Square"""


class Square:
    """Defines a Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Ensures size is an int and is greater than 0

        Parameters:
            size (int): size of the square
            position (tuple): position of the square
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter method for self.__Position private variable"""

        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for self.__position private variable"""

        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns current square area"""

        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character #"""

        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
