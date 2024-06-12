class Figure:
    def dimension(self):
        return None

    def perimetr(self):
        assert self.dimension() == 2
        return None

    def square(self):
        assert self.dimension() == 2
        return None

    def squareSurface(self):
        assert self.dimension() == 3
        return None

    def squareBase(self):
        assert self.dimension() == 3
        return None

    def height(self):
        assert self.dimension() == 3
        return None

    def volume(self):
        if self.dimension() == 2:
            return self.square()
        return None