class Shape(object):
    """The base class from which other classes will inherit """
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_area(self):
        return self._length * self._width

    def calc_perimeter(self):
        return 2 * (self._width + self._length)


square = Shape(2, 3)
print(square.calc_perimeter())
