#!/usr/bin/python3
"""Defines a class"""


class Rectangle:
    """Represents a class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialised whenever an instance is created

           Parameters:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width private instance variable"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width private instance variable

           Parameters:
                value (int): size of the width

           Raises:
                TypeError: If value is not an integer
                ValueError: If value is less than 0
        """

        if not isinstance(value, int): 
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height private instance variable"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for width private instance variable

           Parameters:
                value (int): size of the height

           Raises:
                TypeError: If value is not an integer
                ValueError: If value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
