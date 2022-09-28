#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle class"""

    def __init__(self, width, height):
        """Instantiation for class Rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """String method for Rectangle class"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Represents area of the rectangle"""

        return self.__height * self.__width
