#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size and position of square.
        Args:
            size (int): size of Square
            position (tuple): poisition of Square
        """
        self.size = size
        self.position = position

    def area(self):
        """Computes the area of the Square.
        Returns:
        Area of square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """gets size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter  method that sets the size of square.
        Args:
            value (int): size of Square
        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        @property
        def position(self):
            """gets position of square."""
            return self.__position

        @position.setter
        def position(self, value):
            """position setter method that sets position of Square.
        Args:
            value (tuple): tuple of two positive integer coordinates
        Raises:
            TypeError: If `value` is not a tuple of two positive integers
            """
            if not isinstance(value, tuple):
                raise TypeError("position must be a tuple of 2 positive integer
                s")
            elif len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integer
s")
            elif not isinstance(value[0], int) or not isinstance(value[1], int):
                raise TypeError("position must be a tuple of 2 positive integer
s")
            elif (value[0] < 0 or value[1] < 0):
                raise TypeError("position must be a tuple of 2 positive integer
s")
            else:
                self.__position = value

        def my_print(self):
            """Prints a # representation of square based on size."""

            if self.__size == 0:
                print()
            else:
                for i in range(self.__position[1]):
                    print()
                for j in range(self.__size):
                    print(' ' * self.__position[0], end='')
                    print('#' * self.__size)
