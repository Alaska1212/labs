#трикутник
class Triangle:
    def __init__(self,a: float, b: float,c: float):
        adges = [a, b, c]
        adges.sort()
        a, b, c = adges
        assert a + b > c
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return (self.a + self.b + self.c) / 2

    def area(self) -> float:
        p = self.perimeter()
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    print(t.area())