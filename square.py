from shape import Shape


class Square(Shape):
    """This classs inherits from the super class Shape"""
    def __init__(self, width, length):
        super().__init__(width, length)

square = Square(12, 4)
print(square.calc_area())
