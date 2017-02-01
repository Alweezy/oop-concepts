from shape import Shape


class Cube(Shape):
    def __init__(self,length, width, height):
        self._height = height
        super().__init__(length, width)

    def get_volume(self):
        area = self.calc_area()
        return area * self._height

my_cube = Cube(2, 3, 2)
print(my_cube.get_volume())

