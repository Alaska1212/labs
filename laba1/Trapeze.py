#трапеція
class Trapeze:
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
        return
    #перевірити формулу площі!

if __name__ == '__main__':
    t = Trapeze(8,6,10,5)
    print(t.area())