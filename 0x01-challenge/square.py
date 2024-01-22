#!/usr/bin/python3
"""Module contains the Square class
"""


class square():
    """Square class

    Methods:
    area_of_my_square: calculate area of square
    PerimeterOfMySquare: find perimeter
    """

    def __init__(self, *args, **kwargs):
        """Set values for instances"""
        width = 0
        height = 0

        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Perimeter of Square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Informal repressentation of the square object"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
