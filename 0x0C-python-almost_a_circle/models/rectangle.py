#!/usr/bin/python3
"""Contains a Rectangle class"""
from models.rectangle import Rectangle


class Rectangle(Base):
    """Rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """Getter for width"""

            return self.__width

        @width.setter
        def width(self, value):
            """Setter for width"""

            self.__width = width

        @property
        def height(self):
            """Getter for height"""

            return self.__height

        @height.setter
        def height(self, value):
            """Setter for height"""

            self.__height = height

        @property
        def x(self):
            """Getter for x"""

            return self.__x

        @x.setter
        def x(self, value):
            """Setter for x"""

            self.__X = x

        @property
        def y(self):
            """Getter for y"""

            return self.__y

        @y.setter
        def y(self, value):
            """Setter for y"""

            self.__y = y

