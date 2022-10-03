#!/usr/bin/python3
"""Contains a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """String method for Rectangle class"""

        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}")

    @property
    def width(self):
        """Getter for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """Returns the area value of the Rectangle instance"""

        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle with the character #"""

        for top_offset in range(self.y):
            print("")
        for height in range(self.height):
            for right_offset in range(self.x):
                print(" ", end="")
            for width in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        for idx, val in enumerate(args):
            if idx == 0:
                self.id = val
            elif idx == 1:
                self.width = val
            elif idx == 2:
                self.height = val
            elif idx == 3:
                self.x = val
            elif idx == 4:
                self.y = val

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
