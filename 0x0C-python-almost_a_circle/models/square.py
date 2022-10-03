#!/usr/bin/python3
"""Defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents Square class that inherits from Base class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String special method for Square class"""

        return f"[Square] ({self.id}) {self.x}/{self.y}" \
               f" - {self.width}"

    @property
    def size(self):
        """Getter for size"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""

        for index, arg in enumerate(args):
            if index == 0:
                self.id = arg
            elif index == 1:
                self.width = arg
            elif index == 2:
                self.x = arg
            elif index == 3:
                self.y = arg

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "size":
                self.width = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
