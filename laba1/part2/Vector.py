class Vector:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], Vector):
            vect = args[0]
            self.coords = vect.coords
        else:
            self.coords = args

    def show(self):
        return self.coords

    def dim(self):
        return len(self.coords)

    def module(self):
        sum = 0
        for i in self.coords:
            sum += i**2

        return sum ** 0.5

    def mean(self):
        sum = 0
        for i in self.coords:
            sum += i

        mean = sum / len(self.coords)
        return mean

    def min(self):
        min1 = min(self.coords)
        return min1

    def max(self):
        max1 = max(self.coords)
        return max1
