from Figure import Figure
class Circle(Figure):
    def __init__(self, _r):
        self._r = _r

    def dimension(self):
        return 2

    def perimetr(self):
        assert self.dimension() == 2
        return 2 * 3.14 * self._r

    def square(self):
        return 3.14 * self._r ** 2

    def __str__(self):
        return f'Circle {self._r}'