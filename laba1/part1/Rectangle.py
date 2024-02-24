#прямокутник
class Rectangle:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b)*2

    def area(self):
        return self.a * self.b

if __name__ == '__main__':
    t = Rectangle(3, 4)
    print(t.area())