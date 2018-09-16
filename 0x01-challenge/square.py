#!/usr/bin/python3


class Square():
    """Documentation"""

    def __init__(self, width=None, height=None):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not value:
            raise TypeError('Width cannot be None')
        elif not isinstance(value, int):
            raise TypeError('Width has to be an integer')
        elif value < 1:
            raise ValueError('Width must be greater than 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not value:
            raise TypeError('Height cannot be None')
        elif not isinstance(value, int):
            raise TypeError('Height has to be an integer')
        elif value < 1:
            raise ValueError('Height must be greater than 0')
        else:
            self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
