#прямокутник
class Rectangle:
    def __init__(self, a: float, b: float, c: float, d: float):
        adges = [a, b, c, d]
        adges.sort()
        a, b, c, d = adges
        assert a == b and c == d
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return self.a * self.c

if __name__ == '__main__':
    t = Rectangle(3, 4, 3, 4)
    print(t.area())