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
