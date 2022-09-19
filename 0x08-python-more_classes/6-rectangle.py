#!/usr/bin/python3
"""Defines a class"""


class Rectangle:
    """Represents a class Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialised whenever an instance is created

           Parameters:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """Draws a rectangle using the character #"""

        if self.width == 0 or self.height == 0:
            return ""
        return_string = ""
        for height in range(self.height):
            for width in range(self.width):
                return_string += '#'
            if height < self.height - 1:
                return_string += '\n'
        return return_string

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Runs when an instance is deleted"""

        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self. height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)
