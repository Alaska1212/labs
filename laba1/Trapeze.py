#трапеція
class Trapeze:
    def __init__(self, a: float, b: float, c: float, d: float):
        adges = [a, b, c, d]
        adges.sort()
        a, b, c, d = adges
        assert a != d
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        dr = ((self.d - self.a)**2 + self.c**2 - self.b**2)/(2*(self.d - self.a))
        return ((self.a + self.d)/2) * (self.c**2 - dr**2)**0.5
    #перевірити формулу площі!

if __name__ == '__main__':
    t = Trapeze(8,6,10,5)
    print(t.area())