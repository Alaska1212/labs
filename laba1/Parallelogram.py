#паралелограм
class Parallelogram:
    def __init__(self, a: float, b: float, h: float):
        adges = [a, b, h]
        adges.sort()
        h, a, b = adges
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return (self.a + self.b)*2
    def area(self):
        return (self.h * self.b)

if __name__ == '__main__':
    t = Parallelogram(8, 6, 10)
    print(t.area())