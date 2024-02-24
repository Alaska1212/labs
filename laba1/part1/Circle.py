#круг
import math
class Circle:
    def __init__(self, a: float):
        self.a = a
    def perimeter(self):
        return self.a * 2 * math.pi

    def area(self):
        return self.a ** 2 * math.pi

if __name__ == '__main__':
    t = Circle(8)
    print(t.area())